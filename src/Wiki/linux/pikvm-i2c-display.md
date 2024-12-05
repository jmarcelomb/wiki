# Connect i2c display to DIY pikvm

The main problem is that i2c doesn't come enabled by default.

## Steps

- `su` (default password is `root`)
- `rw` to be able to edit files
- Add `dtparam=i2c_arm=on` to `/boot/config.txt`
- Create a file `/etc/modules-load.d/i2c-dev.conf` with the content `i2c-dev`
- `systemctl enable kvmd-oled kvmd-oled-reboot kvmd-oled-shutdown`
- `ro`
- `reboot`