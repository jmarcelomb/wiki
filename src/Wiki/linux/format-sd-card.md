# How to format an SD-Card in Linux (cli)

```bash
# This command will list all block devices. We need to know which one is the SD-card.
# Should be /dev/sdb.
lsblk

# The numbers in the end indicate the different partitions.
# For example, there might be two partitions: /dev/sdb1 and /dev/sdb2.
# To solve this, we need to delete all partitions and create only one.
sudo fdisk /dev/sdb

# fdisk will open a console.
# Firstly, we enter the command p. This command will list the partitions.
# Secondly, we enter the command d. This command deletes 1 partition. If we want to delete two partitions, we should run this command two times.
# Thirdly, we enter the command n. This command creates 1 partition. We can accept all the default options, which creates one partition with the disk's full size.
# Finally, we enter the command w. This command writes the changes to the disk (it is like committing to a database).

# Now that we have a clean partition, we just need to create the file system.
# For exFAT we use the following command:
mkfs.exfat /dev/sdb1

# If the previous command does not exist, we need to install it:
sudo pacman -Syu exfatprogs
```
