My preferred way to run obsidian will be to have two repositories, one for notes themselves, and then one for settings, which is this one. On each vault, add this repository as a Git submodule, which will load every setting and plugin.

Add this repository to another as a submodule
```shell
# add submodule with SSH
git submodule add git@github.com:cesarnr21/.magma.git

# add submodule with HTTPS
git submodule add https://github.com/cesarnr21/.magma.git

# initialize submodule
git submodule init

# pull the latest commits for the submodule, --remote option might not always work
git submodule update --recursive --remote
```

> currently symlinks (soft links) are not supported by obsidian, so access `.md` in the parent vault, you could hardlink them

Use plugin [Show Hidden Files for Obsidian](https://github.com/polyipseity/obsidian-show-hidden-files). Keep the setting `Detect all file extensions` disable, but on the Show Hidden Files plugin settings enable `Show Hidden Files`

To keep this repository up to date, use
```shell
# pull the latest commits for the submodule, --remote option might not always work
git submodule update --recursive --remote
```

# Some changes for obsidian
---
- Like VSCode, Obsidian has a command palate that opens with `CTRL + P` and quick switcher to open/create files with `SHIFT + O`. Remap these shortcuts to `SHIFT + CTRL + P` for command palate and `CTRL + P` for quick switch, this resembles VSCode more.
- Set `CTRL + SHIFT + T`  to show tags
- Set `CTRL + SHIFT + O` to show file outline
- Set `CTRL + SHIFT + E` to show file explorer
- Set `CTRL + B` to toggle left sidebar (includes file explorer)
- Set `CTRL + J` to toggle right sidebar (includes file outline) 
- Enable vim mode


# TODO
## Vault usage

- [ ] templates or some other kind of shortcut to insert different html code into note (example insert image with html, or side-by-side column)
- [ ] a script that will pull data from all the installed plugins and create a list with all plugins and versions.
- [ ] test using markdown inside HTML
- [ ] How to keep two version branches of the software and bring commits back and forth between two remotes
- [ ] How to switch tabs/groups fast. It would be nice to have all tabs, regardless of whether they are in separate groups or together.
- [ ] setup [obsidian remote](https://github.com/sytone/obsidian-remote) to allow network wide access.



# Working with Git
---
Before the first commit, make sure that the User and Email settings for the local repository are set correctly.
Under the `.magma` repository, do:

```shell
# set correct user name
git config --local user.name "cesarnr21" 
git config --local user.email "cesarnr21@gmail.com" 

# see local settings vs global settings
git config --local --list
git config --global --list

# to ammend a commit with a different author
git commit --amend --author="Author Name <email@address.com>" --no-edit
```

- View the edit/git history of a single file
```shell
# view commits where the file has been edited
git log filename

# to view changes as well, use
git log -p filename

# to show the entire history, including renames, use 
git log --follow -p filename
```


## CHANGELOG and tagging Versions of the Vault
Create tags to keep track of the changes to the `.magma` config repository. Add tags to [CHANGELOG.md](.magma/CHANGELOG.md) files and log unreleased changes.

When tagging a commit for the `.magma` repository, do something like
```shell
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
```shell
obsidian vault version 0.1.0
uses .magma config 0.1.0

- changes
- any changes made to the vault
```

Tagging commits
```shell
# show tags
git tag

# tag the current HEAD
git tag -a {version}

# add a tag to an older commit
git tag -a {version> {commit}

# push commit
git push origin {tag}
# or git push {remote}
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
```shell
fatal: The upstream branch of your current branch does not match
the name of your current branch.  To push to the upstream branch
on the remote, use

    git push origin HEAD:<branch_name>

To push to the branch of the same name on the remote, use

    git push origin HEAD
```

To fix this, use
```shell
git branch --unset-upstream

# then try to push again with 
git push --set-upstream origin <branch_name>
```

## Create Personal Access Tokens
[Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) might be needed in case 

## Access Repository on iOS and iPad devices
There are a few ways to accomplish this. 

One way is to use this [obsidian git plugin](https://github.com/Vinzent03/obsidian-git#mobile), not tested, but currently as of 2025-02-01, the plugin does not support some [git operations, git submodules, and has size restrictions](https://github.com/Vinzent03/obsidian-git?tab=readme-ov-file#restrictions).

A free and open source option is to use [a-shell](https://holzschu.github.io/a-Shell_iOS/) which is an app with an unix-like terminal for iOS and iPad devices.

Finally, there is the [Working Copy](https://workingcopyapp.com/users-guide) app to clone the repositories and then link the repository to a folder that obsidian can access. However, this requires a Pro version of the app which cost money. Also, it requires that app to create and store an SSH key with access to your GitHub account. [This tutorial goes into more details](https://meganesulli.com/blog/sync-obsidian-vault-iphone-ipad/).

For Android, look into [GitSync](https://github.com/ViscousPot/GitSync/wiki)

Since  [a-shell](https://holzschu.github.io/a-Shell_iOS/) is my preferred solution, install it from the App Store.

Keep in mind that while using Obsidian in either iPhone or iPad and using an external keyboard, all shortcuts will work with the `CMD` key instead of `CTRL`.

- [ ] create a script and apple shortcut to automatically use a-Shell to pull the latest changes from GitHub
- [ ] test does it make sense to pull the notes repository into Google Drive on the iPad and iPhone. This would allow to also link files from google drive.

