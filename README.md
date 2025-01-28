My preferred way to run obsidian will be to have two repositories, one for notes themselves, and then one for settings, which is this one. On each vault, add this repository as a Git submodule, which will load every setting and plugin.

Add this repository to another as a submodule

```bash
git submodule add git@github.com:cesarnr21/.magma.git

# add submodule with HTTPS
git submodule add https://github.com/cesarnr21/.magma.git
```

> currently symlinks (soft links) are not supported by obsidian.

To access both this `README.md` and `TODO.md` in the obsidian vault, hardlink them to the root of the vault, and make sure that they are added to the `.gitingore`
```bash
ln .magma/README.md README.md
ln .magma/TODO.md TODO.md
ln .magma/CHANGELOG.md CHANGELOG.md
```

# TODO:
To keep this repository up to date, use
- [ ] how to update this from the root of the parent directory, basically pull the latest commit added to main?, maybe use a `Makefile` and hard link it to the root directory

# Some changes for obsidian
---
- Like VSCode, Obsidian has a command palate that opens with `CTRL + P` and quick switcher to open/create files with `SHIFT + O`. Remap these shortcuts to `SHIFT + CTRL + P` for command palate and `CTRL + P` for quick switch, this resembles VSCode more.
- Set `CTRL + SHIFT + T`  to show tags
- Set `CTRL + SHIFT + O` to show file outline
- Set `CTRL + SHIFT + E` to show file explorer
- Set `CTRL + B` to toggle left sidebar (includes file explorer)
- Set `CTRL + J` to toggle right sidebar (includes file outline) 
- Enable vim mode



# Working with Git
---
## Tagging Versions of the Vault
Tag specific commits in the git history to keep track of major changes on the vault. These could include:
- [ ] Adding/removing a plugin
- [ ] Adding a project or archiving a project from the root of the vault to the `archive` folder.

When tagging a commit for the `.magma` repository, do something like
```bash
obsidian config version 0.1.0
- added plugin from <github>
- any changes made to the vault

active plugins:
- plugin a <version>
- plugin b <version>

active projects
- project a
- project b
- whatever
```

For a note vault that uses this 
```bash
obsidian vault version 0.1.0
uses .magma config 0.1.0

- changes
- any changes made to the vault
```


## CHANGELOG
In Addition to the tags, keep a [CHANGELOG.md](CHANGELOG.md) file to keep track of the changes to the `.magma` config repository.

## Useful commands for editing
- Tagging commits
```bash
# show tags
git tag

# tag the current HEAD
git tag -a <version>

# add a tag to an older commit
git tag -a <version> <commit>

# push commit
git push origin <tag>
# or git push <remote>
```

- View the edit/git history of a single file
```bash
# view commits where the file has been edited
git log filename

# to view changes as well, use
git log -p filename

# to show the entire history, including renames, use 
git log --follow -p filename
```

## Troubleshooting
### Fast-Forward Rebase on GitHub
I really like the `--ff-only` merge strategy on BitBucket, which will rebase the `main` branch and bring over the commit history from the source branch without a merge commit.

GitHub does not support this option, there is a potential work around.
1. Rebase and resolve any conflicts on between the target and source branch
2. Open a pull Request
3. On the local git repository, `git fetch` the remote source branch then `git checkout <target>`.
4. `git merge <origin/source` and then `git push`. The pull request will automatically be closed, and you will have a similar merge strategy to `--ff-only`

### Branching Issues/No upstream branch
Sometimes there  will be an error that looks like
```bash
fatal: The upstream branch of your current branch does not match
the name of your current branch.  To push to the upstream branch
on the remote, use

    git push origin HEAD:<branch_name>

To push to the branch of the same name on the remote, use

    git push origin HEAD
```

To fix this, use
```bash
git branch --unset-upstream

# then try to push again with 
git push --set-upstream origin <branch_name>
```


# Files
---
Look at [rclone](/guides/rclone.md)


# Plugins
---
> *There does not seem to much of a difference between installing plugins from the Obsidian Community Plugins Page and from Source*

Installing Plugins from source [YouTube tutorial](https://www.youtube.com/watch?v=ffGfVBLDI_0) tldr; go to releases on the plugins repository and download the `main.js` and `manifest.json` files. Add them to the `.magma/plugins/plugin-name` path and then enable them in community plugins.

### vim and .vimrc
> *Source: [obsidian vimrc support](https://github.com/esm7/obsidian-vimrc-support?tab=readme-ov-file#maintainer-needed)*

It best to experiment in obsidian with the vim command prompt `SHIFT` + `:`. To load and test changes from the `.obsidian.vimrc` file, just use the command `RELOAD APP WITHOUT SAVING`.


