# Neovim

To access my Neovim config [click here.](https://github.com/jmarcelomb/nvim)

* * *

## Execute normal mode commands using text:
We can execute commands using `normal` or `norm` for short:

```
:norm[al][!] {commands}
```

If the `!` is given, mappings will not be used. Without it, when this command is called from a non-remappable mapping (|:noremap|), the argument can be mapped anyway.

```
:normal ! yyp
:norm ! itest
```

Once Vim enters insert mode with the i in `itest<esc>` all bets are off and printable characters lose their special functions. To get an `<Esc>` within your `:normal`, you need to either use `<C-V><Esc>` (literally type Ctrl+V followed by the Escape key) or alternatively use `:execute` plus backslash escaping:

```
:exe "norm itest\<esc>"
:exe "norm i\<cr>another\<cr>example\<esc>yipP"
```

***

## Macros
**Fun trick**: we can add the macro call to the end of your recording macro to create a self calling recursive macro, that will just run until the end of the file, no need to guess how many times to run the macro! 

Another common pattern is `:g/pattern/norm! @q` to execute once on each line that has pattern in it.

## Go back in time (`:earlier`)

```
:earlier 1m
```

## Insert commands with r(ead)
In command mode you can do `:r ! terminal_command`. `r` is the short version of the command `read`.
For example, if you do `r: ! ls` It will append the `ls` content in the current cursor position or selection. 

## Motions

`f`(ind) - find forward
`F`(ind) - find backwards
Example: `f,` - `f`(ind) comma

`t`(il) - Til forward
`T`(il) - Til backwards
Example: `yt,` - yank `t`(il) comma

`*` - forward search of word under the cursor
`#` - backwards search of word under the cursor

`gv` - starts visual mode with the previous visual selection. This is useful if you mess up some command, you just u to undo and gv to reselect and try again, or if you want to perform multiple operations on the same visual block

---
## Regex pattern to register

You can do this with a substitute command.

```
:%s/regex/\=setreg('A', submatch(0))/n
```

This will append register a to whatever the regex matched. The n flag will run the command in a sandbox so nothing will actually get replaced but the side effects of the statement will happen.

You probably want to empty the register first with
```
:let @a=''
```

If you want to place a new line in-between each match:
```
:let @a='' | %s/regex/\=setreg('A', submatch(0) . "\n")/n 
```
---
## Delete all lines containing a pattern

The command `g` is very useful for acting on lines that match a pattern. You can use it with the `d` command, to delete all lines that contain a particular pattern, or all lines that do not contain a pattern.

For example, to delete all lines containing *"profile"* (remove the `/d` to show the lines that the command will delete):

```
:g/profile/d
```

More complex patterns can be used, such as deleting all lines that are empty or that contain only whitespace:

```
:g/^\s*$/d
```

To delete all lines that do not contain a pattern, use `g!`, like this command to delete all lines that are not comment lines in a Vim script:

```
:g!/^\s*"/d
```

Note that g! is equivalent to `v`, so you could also do the above with:

```
:v/^\s*"/d
```

The next example shows use of `\|` ("or") to delete all lines except those that contain *"error"* or *"warn"* or *"fail"* (`:help pattern`):

```
:v/error\|warn\|fail/d
```

`g` can also be combined with a range to restrict it to certain lines only. For example to delete all lines containing *"profile"* from the current line to the end of the file:

```
:.,$g/profile/d
```

## Install latest version in Linux script

```bash
#!/usr/bin/env bash
 
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz
tar -xzf nvim-linux-x86_64.tar.gz
rm -f nvim-linux-x86_64.tar.gz
echo "Add to your shell config"
printf 'export PATH="$PATH:%s/nvim-linux-x86_64/bin"\n' "$(pwd)"
```

Reference [here](https://vim.fandom.com/wiki/Delete_all_lines_containing_a_pattern).
