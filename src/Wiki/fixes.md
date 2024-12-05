# Fixes for weird problems I might need again

## Sound crackling and suspending after a short time (when idle)

Note: I don't know how to fix the crackling when the intel_hda_controller
comes online. This is only a mitigation of the issue.

It makes that sound when going idle, because of the power saving feature.
With `pacmd list-sinks` it's possible to see:

```bash
state: SUSPENDED
suspend cause: IDLE
```

`echo 0 > /sys/module/snd_hda_intel/parameters/power_save` will disable
the power saving feature, thus avoiding the crackling/popping every time
the sink comes on/off.

To make it persistent, I create a file in `/etc/modprobe.d` called `audio_pop.conf` with the contents `options snd_hda_intel power_save=0`.

## Weird occasional latency problems with Bluetooth devices

This seems to be an issue with the power manager. I fixed it by putting the following on a `bluetooth_latency_fix.conf` in `/etc/modprobe.d` (and restarting):

```bash
options usbcore autosuspend=-1
options btusb enable_autosuspend=0
```

## Application not recognizing the display environment

Edit `/etc/pam.d/system-login` as sudo and append `type=x11`:

`-session   optional   pam_systemd.so`

becomes

`-session   optional   pam_systemd.so  type=x11`


## Mouse wouldn't move camera in Dark Souls II (wine/proton)

When running Dark Souls II in proton, the mouse would be recognised and work
on the menus, but I wasn't able to move the camera with it (the arrow keys moved
the camera and the left and right mouse buttons performed attacks).

To fix it, I ran the following command inside the profile's pfx directory:

`
printf "REGEDIT4\n[HKEY_CURRENT_USER\Software\Wine\\\Explorer]\n\"Desktop\"=\"Default\"\n[HKEY_CURRENT_USER\Software\Wine\\\Explorer\Desktops]\n\"Default\"=\"1920x1080\"\n[HKEY_CURRENT_USER\Software\Wine\\X11 Driver]\n\"GrabFullscreen\"=\"N\"" >> temp.reg && find -name "pfx" | xargs readlink -f | xargs -I{} env WINEPREFIX={} regedit temp.reg && rm temp.reg
`

## Tor service failing to initialize

I don't know which update made this starting to happen, but the Tor hidden service
configuration on my server's website started requiring a new option (on Arch).
It was now necessary to set `User tor` on `/etc/tor/torrc`. This user can probably
change between distributions/install processes/use cases.

## GRUB menu not showing after fresh installing

In the case of some motherboard manufacters/models (in my case MSI), the UEFI firmware requires the bootable file at a known location before they will show UEFI NVRAM boot entries. There are 2 solutions at the time of writing:

The first solution is to install GRUB at the default/fallback boot path:

`grub-install --target=x86_64-efi --efi-directory=esp --removable`

Alternatively, you can move an already installed GRUB EFI executable to the default/fallback path:

`mv esp/EFI/grub esp/EFI/BOOT`
and then
`mv esp/EFI/BOOT/grubx64.efi esp/EFI/BOOT/BOOTX64.EFI`
