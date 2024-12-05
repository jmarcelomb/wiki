# Make raspberry pi file system read-only

Crashes + log messages like this imply damaged SD card/file system corruption:
```
end_request: I/O error, dev mmcblk0, sector 148225
mmcblk0: error -110 transfering data, sector 148226, nr 254, response 0x900, card status 0xb00
```

## SD card backup

You can create a backup of the SD card by connecting the SD card to a computer
and running dd (e.g.: sd card is /dev/sdc):  
`sudo dd if=/dev/sdc of=PiSDBackup.img status=progress`

To reverse the process, use:  
`sudo dd if=PiSDBackup.img of=/dev/sdc status=progress`

## Removing packages and updating

  - Remove the following packages: `sudo apt-get remove --purge triggerhappy logrotate dphys-swapfile`
  - Clean up your packages: `sudo apt-get autoremove --purge`
  - Update the system's packages: `sudo apt-get update && apt-get upgrade`

## Disable swap and set the file system to read-only

Append the following to the **/boot/cmdline.txt** file: `fastboot noswap ro`

This line should now look similar to this:  
`dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait fastboot noswap ro`

## Replace log manager

We will remove the standard syslog output of log files to /var/log and instead replace it with the busybox in-memory logger:  
```
sudo apt-get install busybox-syslogd
sudo apt-get remove --purge rsyslog
```

Note: Use `sudo logread` to check system logs.

## Make the file-systems read-only and add the temporary storage

Update the file **/etc/fstab** and add the `,ro` flag to all block devices.
The updated file should look like this:  
```
proc                  /proc     proc    defaults             0     0
PARTUUID=fb0d460e-01  /boot     vfat    defaults,ro          0     2
PARTUUID=fb0d460e-02  /         ext4    defaults,noatime,ro  0     1
```

Also add the entries for the temporary file system at the end of the file:  
```
tmpfs        /tmp            tmpfs   nosuid,nodev         0       0
tmpfs        /var/log        tmpfs   nosuid,nodev         0       0
tmpfs        /var/tmp        tmpfs   nosuid,nodev         0       0
```

## Move some system files to temp filesystem

Warning: This part is different from previous Raspbian versions (Stretch etc.). On Raspbian Buster,
do not move the **/var/lock** and **/var/run** directories as they are already symlinked
to tmpfs directories. You can read more about these changes in the Debian Buster
tmpfs documentation.

```
sudo rm -rf /var/lib/dhcp /var/lib/dhcpcd5 /var/spool /etc/resolv.conf
sudo ln -s /tmp /var/lib/dhcp
sudo ln -s /tmp /var/lib/dhcpcd5
sudo ln -s /tmp /var/spool
sudo touch /tmp/dhcpcd.resolv.conf
sudo ln -s /tmp/dhcpcd.resolv.conf /etc/resolv.conf
```

## Update the systemd random seed

Link the random-seed file to the tmpfs location:  
```
sudo rm /var/lib/systemd/random-seed
sudo ln -s /tmp/random-seed /var/lib/systemd/random-seed
```

Edit the service configuration file **/lib/systemd/system/systemd-random-seed.service**
to have the file created on boot. Add the line `ExecStartPre=/bin/echo "" >/tmp/random-seed`
under the **[Service]** section.

The modified [Service] section should look like this:  
```
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStartPre=/bin/echo "" >/tmp/random-seed
ExecStart=/lib/systemd/systemd-random-seed load
ExecStop=/lib/systemd/systemd-random-seed save
TimeoutSec=30s
```

## Add commands to switch between RO and RW 

Append your **.bashrc** file:  
```
set_bash_prompt() {
  fs_mode=$(mount | sed -n -e "s/^\/dev\/.* on \/ .*(\(r[w|o]\).*/\1/p")
  PS1='\[\033[01;32m\]\u@\h${fs_mode:+($fs_mode)}\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
}
PROMPT_COMMAND=set_bash_prompt
alias ro='sudo mount -o remount,ro / ; sudo mount -o remount,ro /boot'
alias rw='sudo mount -o remount,rw / ; sudo mount -o remount,rw /boot'
```

## Make file system go back to read-only on log out

Append to the **/etc/bash.bash_logout** file:  
```
mount -o remount,ro /
mount -o remount,ro /boot
```

## Reboot the system

`sudo reboot now`

## Source

[Medium raspberry pi post](https://medium.com/swlh/make-your-raspberry-pi-file-system-read-only-raspbian-buster-c558694de79)