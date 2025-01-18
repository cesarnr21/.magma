My preferred way to run obsidian will be to have two repositories, one for notes themselves, and then one for settings, which is this one. On each vault, add this repository as a Git submodule, which will load every setting and plugin.

# Some changes for obsidian
---
- Like VSCode, Obsidian has a command palate that opens with `CTRL + P` and quick switcher to open/create files with `SHIFT + O`. Remap these shortcuts to `SHIFT + CTRL + P` for command palate and `CTRL + P` for quick switch, this resembles VSCode more.
- Set `CTRL + B` to toggle left sidebar (includes file explorer)
- Set `CTRL + J` to toggle right sidebar (includes file outline) 
- Enable vim mode



# Working with Git
---
## Tagging Versions of the Vault
Tag specific commits in the git history to keep track of major changes on the vault. These could include:
- [ ] Adding/removing a plugin
- [ ] Adding a project or archiving a project from the root of the vault to the `archive` folder.

When a tagging a commit, do something like
```bash
obsidian vault version 0.1.0
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



# Plugins
---
Installing Plugins from source [YouTube tutorial](https://www.youtube.com/watch?v=ffGfVBLDI_0)

New plugins
- [Kanan Board Tutorial](https://www.youtube.com/watch?v=13mElDSs0a8)
- DataView
- Tasks plugin







