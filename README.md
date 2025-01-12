Obsidian vault for notes.
### Some changes for obsidian
- Like VSCode, Obsidian has a command palate that opens with `CTRL + P` and quick switcher to open/create files with `SHIFT + O`. Remap these shortcuts to `SHIFT + CTRL + P` for command palate and `CTRL + P` for quick switch, this resembles VSCode more.
- Set `CTRL + B` to toggle left sidebar (includes file explorer)
- Set `CTRL + J` to toggle right sidebar (includes file outline) 
- Enable vim mode


### Working with Git
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

## Plugins
Installing Plugins from source [YouTube tutorial](https://www.youtube.com/watch?v=ffGfVBLDI_0)

[Kanan Board Tutorial](https://www.youtube.com/watch?v=13mElDSs0a8)








