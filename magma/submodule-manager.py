#!/usr/bin/env python3
"""
Tracks and update releases for git submodules. Some projects are only available to download 
by getting them from their releases page. This script:

  1. Reads .gitmodules to find every submodule (path + GitHub URL).
  2. Looks at the commit each submodule is currently pinned to.
  3. Finds the GitHub release/tag that commit corresponds to, and downloads
     that release's assets.
  4. Optionally (--latest --update): instead of matching the pinned commit,
     downloads the plugin's *latest* release and moves the submodule's
     pinned commit forward to that release's tag (i.e. `git add`s the new
     gitlink so the parent repo records the update).

# current biggest limiation is that some submodules do not use releases
# TODO: if no releases, then fetch and update to latest available commit
"""

import argparse
import functools
import json
import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

from magma import REPO_ROOT, setup_logging

GITHUB_URL = "https://api.github.com"


logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--debug", action="store_true", help="use debug mode for logging")
    parser.add_argument("--list", action="store_true", help="list all submodules, commits, and release tags")
    parser.add_argument("--pull", action="store_true", help="download current release assets")
    parser.add_argument("--fetch", action="store_true", help="get latest release for each submodule")
    parser.add_argument("--update", action="store_true", help="Get and download the latest release instead and update the submodule to new release tag")
    parser.add_argument("--token", help="GitHub API Token to bypass rate limiting. (recommended while developing/testing)")
    args = parser.parse_args()

    setup_logging(args.debug)
    logger.debug(f"configuration set {vars(args)}")

    session = gh_session(args.token)

    submodules = parse_gitmodules(session)

    if args.list:
        # TODO: implement function top pretty print this
        # pretty_print(submodules)
        print("submodules:")
        print(json.dumps(submodules, indent=4))

    for sub in submodules:
        # less of these
        path = sub.get("path")
        url = sub.get("url")

        if not path or not url:
            logger.warning("Missing path or url in .gitmodules")
            continue

        try:
            if args.fetch or args.update:
                latest_release = get_latest_release(session, sub["owner"], sub["repo"])

                if sub["release"] == latest_release["tag_name"]:
                    logger.info(f"{sub['name']} is already at latest release: {sub['release']}")
                else:
                    logger.info(f"{sub['name']} -> Current release {sub['release']}, latest: {latest_release['tag_name']}")

            if args.pull or args.update:
                logger.info(f"  Pinned commit: {sub['commit']}")
                dest_dir = REPO_ROOT / path

                if args.update:
                    # if update is true, then latest_release was defined up there, this variable will always be bound at runtime
                    sub["release"] = latest_release["tag_name"] # pyright: ignore[reportPossiblyUnboundVariable]
                    update_submodule_to_tag(path, sub["release"])

                release_assets = get_release_by_tag(session, sub["owner"], sub["repo"], sub["release"])
                download_release_assets(session, release_assets, dest_dir)

        except requests.HTTPError as e:
            logger.error(f"GitHub API error: {e}, skipping.")
            continue
        except subprocess.CalledProcessError as e:
            logger.error(f"Git error: {e}, skipping.")
            continue
        except Exception as e:
            logger.error(f"another exception happenned {e}, skipping.")
            continue


def parse_gitmodules(session: requests.Session) -> list[dict]:
    """Parse .gitmodules using `git config` so we handle the format correctly."""
    gitmodules_file = REPO_ROOT / ".gitmodules"
    if not gitmodules_file.exists():
        logger.error(f"No .gitmodules found at {gitmodules_file}")
        sys.exit(1)

    result = subprocess.run(
        ["git", "config", "--file", str(gitmodules_file), "--list"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    submodules = {}
    for line in result.stdout.splitlines():
        key, _, value = line.partition("=")
        m = re.match(r"submodule\.(.+)\.(path|url|branch)$", key)
        if not m:
            continue
        name, field = m.group(1), m.group(2)

        # dictionary is created here
        submodules.setdefault(name, {"name": name})[field] = value

    for sub in submodules:
        commit = get_submodule_commit(submodules[sub]["path"])
        owner, repo = parse_owner_repo(submodules[sub]["url"])
        submodules[sub]["commit"] = commit
        submodules[sub]["owner"] = owner
        submodules[sub]["repo"] = repo

        try:
            submodules[sub]["release"] = find_tag_for_commit(session, owner, repo, commit)

        except requests.HTTPError as e:
            logger.error(f"  GitHub API error: {e}")
            submodules[sub]["release"] = None
            continue
        except subprocess.CalledProcessError as e:
            logger.error(f"  Git error: {e}")
            submodules[sub]["release"] = None
            continue
        except Exception as e:
            logger.error(f"another exception happenned {e}")
            submodules[sub]["release"] = None
            continue

    if not submodules:
        logger.info("No matching submodules found.")
        sys.exit(1)

    return list(submodules.values())


def pretty_print(contents: dict) -> None:
    pass


@functools.cache
def get_submodule_commit(submodule_path: str) -> str:
    """Get the gitlink commit sha the parent repo has pinned for a submodule,
    without requiring the submodule to be initialized."""
    result = subprocess.run(
        ["git", "ls-tree", "HEAD", "--", submodule_path],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    line = result.stdout.strip()
    if not line:
        raise Exception(f"Could not determine pinned commit for {submodule_path}")

    # format: "160000 commit <sha>\t<path>"
    parts = line.split()
    if len(parts) < 3:
        logger.error(f"  Could not determine pinned commit for {submodule_path}")
        raise Exception()

    return parts[2]


def parse_owner_repo(url: str) -> tuple[str, str]:
    """Extract (owner, repo) from a GitHub submodule URL, https or ssh style."""
    url = url.strip()
    if url.endswith(".git"):
        url = url[:-4]

    if url.startswith("git@"):
        # git@github.com:owner/repo
        path = url.split(":", 1)[-1]
    else:
        parsed = urlparse(url)
        path = parsed.path.lstrip("/")

    parts = path.split("/")
    if len(parts) < 2:
        raise Exception()

    return parts[-2], parts[-1]


def gh_session(token: str | None) -> requests.Session:
    s = requests.Session()
    headers = {"Accept": "application/vnd.github+json"}
    token = token or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    s.headers.update(headers)
    return s


def gh_get_all_pages(session: requests.Session, url: str, params=None):
    """Follow GitHub pagination (Link header)."""
    items = []
    params = dict(params or {})
    params.setdefault("per_page", 100)
    next_url = url
    while next_url:
        resp = session.get(next_url, params=params if next_url == url else None)
        resp.raise_for_status()
        items.extend(resp.json())
        next_url = resp.links.get("next", {}).get("url")
    return items


@functools.cache
def find_tag_for_commit(session, owner, repo, sha) -> str:
    """Find the tag name whose commit matches `sha`. Returns tag name or None."""
    tags = gh_get_all_pages(session, f"{GITHUB_URL}/repos/{owner}/{repo}/tags")
    for t in tags:
        if t.get("commit", {}).get("sha") == sha:
            return t["name"]

    raise Exception(
            f"  No tag matches pinned commit {sha[:10]} for {owner}/{repo}. "
            f"(It may be an untagged commit ahead of the last release.) Skipping."
        )


@functools.cache
def get_release_by_tag(session: requests.Session, owner: str, repo: str, tag: str) -> dict:
    resp = session.get(f"{GITHUB_URL}/repos/{owner}/{repo}/releases/tags/{tag}")
    if resp.status_code == 404:
        raise Exception(f"Tag {tag} has no published GitHub release")

    resp.raise_for_status()
    return resp.json()


@functools.cache
def get_latest_release(session: requests.Session, owner: str, repo: str) -> dict:
    resp = session.get(f"{GITHUB_URL}/repos/{owner}/{repo}/releases/latest")
    if resp.status_code == 404:
        raise Exception(f"No releases found for {owner}/{repo}")

    resp.raise_for_status()
    return resp.json()


@functools.cache
def get_tag_commit_sha(session, owner, repo, tag):
    """Resolve a tag name to the commit sha it points to."""
    resp = session.get(f"{GITHUB_URL}/repos/{owner}/{repo}/tags")
    resp.raise_for_status()
    for t in resp.json():
        if t["name"] == tag:
            return t["commit"]["sha"]
    return None


def download_release_assets(session: requests.Session, release_assets: dict, dest_dir: Path) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    assets = release_assets.get("assets", [])

    if not assets:
        # Fall back to the source zip if the release has no built assets
        zip_url = release_assets.get("zipball_url")
        if zip_url:
            logger.info(f"    No binary assets; downloading source zip instead.")
            _download_file(session, zip_url, dest_dir / f"{release_assets['tag_name']}-source.zip")
        return

    for asset in assets:
        name = asset["name"]
        url = asset["url"]  # API asset URL; needs Accept: application/octet-stream
        dest = dest_dir / name
        logger.info(f"    Downloading {name} ...")
        headers = {"Accept": "application/octet-stream"}
        resp = session.get(url, headers=headers, stream=True, allow_redirects=True)
        resp.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
    logger.info(f"    Saved to {dest_dir}")


def _download_file(session: requests.Session, url: str, dest: Path):
    resp = session.get(url, stream=True)
    resp.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)


def update_submodule_to_tag(submodule_path: str, tag: str) -> None:
    """Rewrites the submodule's working tree + stages the gitlink in the parent repo's index. 
    Keep in mind that it does NOT commit the new commit for you"""

    full_path = REPO_ROOT / submodule_path

    if not (full_path / ".git").exists():
        logger.info(f"Submodule not initialized at {full_path}; running `git submodule update --init`...")
        subprocess.run(
            ["git", "submodule", "update", "--init", "--", submodule_path],
            cwd=REPO_ROOT,
            check=True,
        )

    subprocess.run(["git", "fetch", "--tags"], cwd=full_path, check=True)
    subprocess.run(["git", "checkout", f"tags/{tag}"], cwd=full_path, check=True)

    subprocess.run(["git", "add", submodule_path], cwd=REPO_ROOT, check=True)
    logger.info(f"Updated {submodule_path} -> {tag} and staged the change in the parent repo.")
    logger.info(f"    (Not committed automatically -- review and commit when ready.)")


if __name__ == "__main__":
    main()
