# Script help message

Idea taken from [here](https://samizdat.dev/help-message-for-shell-scripts/).

## How it works

We just need to add comments right next to the shebang with the help text. Each line should
start with `###`.

```bash
#!/bin/sh
### requires maim and xclip
### Args:
### "snip" - take a snip and pass it to the clipboard
### "picker" - color picker (needs work)
### "current" - snip current active window
### "screenshot" - take a fullscreen screenshot and save it in a file
### no args - dmenu arg selection
```

## Functions

Use this one in your shell to get a list of your scripts and easily select one. You'll see the help text of the one you select.

```bash
help() {
  path="$(find "${SCRIPTS}"/* -type f -print0 | fzf --read0 --print0)"
  [ ! -f "$path" ] && return
  sed -rn 's/^### ?//;T;p' "$path"
}
```

This one is useful to call in a script when ''-h'' is passed or no arguments are given ($0 will expand to the name of the script).

```bash
help() {
  sed -rn 's/^### ?//;T;p' "$0"
}
```
