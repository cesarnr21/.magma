My preferred way to run obsidian will be to have two repositories, one for notes themselves, and then one for settings, which is this one. On each vault, add this repository as a Git submodule, which will load every setting and plugin.

Add this repository to another as a submodule
```bash
# add submodule with SSH
git submodule add git@github.com:cesarnr21/.magma.git

# add submodule with HTTPS
git submodule add https://github.com/cesarnr21/.magma.git

# initialize submodule
git submodule init

# pull the latest commits for the submodule, --remote option might not always work
git submodule update --recursive --remote
```

> currently symlinks (soft links) are not supported by obsidian.

~~To access both this `README.md` and `TODO.md` in the obsidian vault, hardlink them to the root of the vault, and make sure that they are added to the `.gitingore`~~
```bash
ln .magma/README.md README.md
ln .magma/TODO.md TODO.md
ln .magma/CHANGELOG.md CHANGELOG.md
```

On another hand, look into using this plugin [Show Hidden Files for Obsidian](https://github.com/polyipseity/obsidian-show-hidden-files). Keep the setting `Detect all file extensions` disable, but on the Show Hidden Files plugin settings enable `Show Hidden Files`

To keep this repository up to date, use
```bash
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



# Working with Git
---
Before the first commit, make sure that the User and Email settings for the local repository are set correctly.
Under the `.magma` repository, do:

```bash
# set correct user name
git config --local user.name "cesarnr21" 
git config --local user.email "cesarnr21@gmail.com" 

# see local settings vs global settings
git config --local --list
git config --global --list

# to ammend a commit with a different author
git commit --amend --author="Author Name <email@address.com>" --no-edit
```


## Tagging Versions of the Vault
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

## Access Repository on iOS and iPad devices
There are a few ways to accomplish this. 

One way is to use this [obsidian git plugin](https://github.com/Vinzent03/obsidian-git#mobile), not tested, but currently as of 2025-02-01, the plugin does not support some [git operations, git submodules, and has size restrictions](https://github.com/Vinzent03/obsidian-git?tab=readme-ov-file#restrictions).

A free and open source option is to use [a-shell](https://holzschu.github.io/a-Shell_iOS/) which is an app with an unix-like terminal for iOS and iPad devices.

Finally, there is the [Working Copy](https://workingcopyapp.com/users-guide) app to clone the repositories and then link the repository to a folder that obsidian can access. However, this requires a Pro version of the app which cost money. Also, it requires that app to create and store an SSH key with access to your GitHub account. [This tutorial goes into more details](https://meganesulli.com/blog/sync-obsidian-vault-iphone-ipad/).

For Android, look into [GitSync](https://github.com/ViscousPot/GitSync/wiki)

Since  [a-shell](https://holzschu.github.io/a-Shell_iOS/) is my preferred solution, install it from the App Store.

Keep in mind that while using Obsidian in either iPhone or iPad and using an external keyboard, all shortcuts will work with the `CMD` key instead of `CTRL`.

#todo create a script and apple shortcut to automatically use a-Shell to pull the latest changes from GitHub
#todo does it make sense to pull the notes repository into Google Drive on the iPad and iPhone. This would allow to also link files from google drive.


# Files
---
Look at [rclone](https://github.com/cesarnr21/notes/blob/main/guides/rclone.md) to see how sync google drive files with the local file system.


# Plugins
---
> *There does not seem to much of a difference between installing plugins from the Obsidian Community Plugins Page and from Source*

Installing Plugins from source [YouTube tutorial](https://www.youtube.com/watch?v=ffGfVBLDI_0) tldr; go to releases on the plugins repository and download the `main.js` and `manifest.json` files. Add them to the `.magma/plugins/plugin-name` path and then enable them in community plugins.

### vim and .vimrc
> *Source: [obsidian vimrc support](https://github.com/esm7/obsidian-vimrc-support?tab=readme-ov-file#maintainer-needed)*

It best to experiment in obsidian with the vim command prompt `SHIFT` + `:`. To load and test changes from the `.obsidian.vimrc` file, just use the command `RELOAD APP WITHOUT SAVING`.

### Obsidian Jupyter
> *GitHub: [obsidian-jupyter](https://github.com/MaelImhof/obsidian-jupyter)*

#todo tested this plugin on 2025-02-02, and it seems like it will need more work. At the moment it is in beta, and the Jupyter notebook view was messed up and also crashed the obsidian client.

### Excalidraw
> *Quick Overview: [The Excalidraw-Obsidian Showcase: 57 key features in just 17 minutes](https://www.youtube.com/watch?v=P_Q6avJGoWI) and also most of his videos are about doing specific things with Excalidraw and obsidian. This [playlist specifically is a good simple overview](https://www.youtube.com/playlist?list=PL6mqgtMZ4NP1t9IQ6SsuW-cRf8rjA6wrI)*

Excalidraw is an open source virtual whiteboard. Excalidraw also has libraries and scripts that are external to obsidian that will add symbols and functionality to the plugin. See [Excalidraw Libraries here](https://libraries.excalidraw.com/?theme=light&sort=default)

Mainly try to export using `PNG` instead of `SVG` since it's a bit simpler.

Also, add `drafts` folder to `.gitignore` in the parent vault. To insert LaTex formulas, use the command `Insert LaTex Formula`.

> TBH: the Excalidraw plugin is more complex than the Canvas, but for several things it would be better

