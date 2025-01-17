# Neovim

To access my Neovim config [click here.](https://github.com/jmarcelomb/nvim)

* * *

## Execute normal mode commands using text:
We can execute commands using `normal` or `norm` for short:

```bash
:norm[al][!] {commands}
```

If the `!` is given, mappings will not be used. Without it, when this command is called from a non-remappable mapping (|:noremap|), the argument can be mapped anyway.

```bash
:normal ! yyp
:norm ! itest
```

Once Vim enters insert mode with the i in `itest<esc>` all bets are off and printable characters lose their special functions. To get an `<Esc>` within your `:normal`, you need to either use `<C-V><Esc>` (literally type Ctrl+V followed by the Escape key) or alternatively use `:execute` plus backslash escaping:

```bash
:exe "norm itest\<esc>"
:exe "norm i\<cr>another\<cr>example\<esc>yipP"
```

***

## Macros
**Fun trick**: we can add the macro call to the end of your recording macro to create a self calling recursive macro, that will just run until the end of the file, no need to guess how many times to run the macro! 

Another common pattern is `:g/pattern/norm! @q` to execute once on each line that has pattern in it.

## Go back in time (`:earlier`)

```bash
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
