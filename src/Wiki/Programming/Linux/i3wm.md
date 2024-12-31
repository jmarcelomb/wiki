# i3wm

Created time: January 14, 2023 11:14 PM
Last edited time: January 21, 2024 1:09 PM

`vim ~/.config/i3/config`

`$mod` refers to the modifier key (alt by default)

## General

- `startx i3` start i3 from command line
- `$mod+<Enter>` open a terminal
- `$mod+d` open dmenu (text based program launcher)
- `$mod+r` resize mode ( or to leave resize mode)
- `$mod+shift+e` exit i3
- `$mod+shift+r` restart i3 in place
- `$mod+shift+c` reload config file
- `$mod+shift+q` kill window (does normal close if application supports it)

## Windows

- `$mod+w` tabbed layout
- `$mod+e` vertical and horizontal layout (switches to and between them)
- `$mod+s` stacked layout
- `$mod+f` fullscreen

## Moving Windows

- `$mod+shift+<direction key>` Move window in *direction* (depends on direction keys settings)

## How to add screen brightness keys:

1. `sudo apt install light`
2. `sudo chmod +s /usr/bin/light`
3. Add to i3 config:

	```bash
	bindsym XF86MonBrightnessUp exec --no-startup-id light -A 1 # increase screen 
	brightnessbindsym XF86MonBrightnessDown exec --no-startup-id light -U 1 # decrease screen brightness
	```
