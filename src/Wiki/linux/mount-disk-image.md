# Mount disk image files

This comes up when I want to access old backups of my Raspberry Pi's sd card images (obtained through `dd`). The problem of mounting this comes from the existance of multiple partitions. I do the following so I don't have to deal with inputing the partition's offset:

```bash
sudo losetup -P /dev/loop0 steamdeck.img
sudo mount /dev/loop0p8 steamdeck/
```

This would mount the 8th partition of my steam deck's disk image on the `steamdeck/` directory.

After using the `losetup` command, you can use `lsblk` or `fdisk` to inspect the partitions' sizes and select the one you want.
