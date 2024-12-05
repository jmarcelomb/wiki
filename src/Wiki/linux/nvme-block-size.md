# NVME logical block size configuration

Most SSDs report a non-optimal logical block size, typically 512 bytes, for compatibility reasons.

## Querying

Using the `nvme` cli tool, you can query the supported sizes for your devices and their relative perfomance, e.g.:

```bash
nvme id-ns -H /dev/nvme0n1 | grep "Relative Performance"
# ---
LBA Format  0 : Metadata Size: 0   bytes - Data Size: 512 bytes - Relative Performance: 0x2 Good (in use)
LBA Format  1 : Metadata Size: 0   bytes - Data Size: 4096 bytes - Relative Performance: 0x1 Better
```

or using `smartctl` (smaller Rel_Perf is better):

```bash
smartctl -c /dev/nvme0n1
# ---
...
Supported LBA Sizes (NSID 0x1)
Id Fmt  Data  Metadt  Rel_Perf
 0 +     512       0         2
 1 -    4096       0         1
...
```

## Formatting

Do something like `nvme format --lbaf=1 /dev/nvme0n1` where the `--lbaf` option is the ID of the format that you want. Note that doing this will erase everything from your disk.