# Cross-Compilation of Linux Kernel and Debug with QEMU and GDB

In the following tutorial it uses `LLVM=1` because I wanted to use LLVM to compile because I was using rust for linux. 

# Kernel Build

```bash
make LLVM=1 ARCH=x86_64 menuconfig
```

Kernel hacking → **Compile the Kernel with debug info**
Kernel hacking → **Provide GDB scripts for Kernel debugging**

```bash
make LLVM=1 ARCH=x86_64 CROSS_COMPILE=x86_64-unknown-linux-gnu -j$(nproc)
```

# Buildroot

```bash
git clone https://github.com/buildroot/buildroot
cd buildroot
make LLVM=1 ARCH=x86_64 menuconfig
```

Target Options → Target Architecture → x86_64

Filesystem images → ext2/3/4 root file system → ext4

```bash
make LLVM=1 ARCH=x86_64 CROSS_COMPILE=x86_64-unknown-linux-gnu -j$(nproc)
```

# QEMU

## Installing

```bash
sudo apt install qemu qemu-system
```

To boot the kernel using the root filesystem generated by Buildroot, run the following command:

```bash
BUILDROOT_PATH=../buildroot
qemu-system-x86_64 \
    -kernel arch/x86/boot/bzImage \
    -boot c \
    -m 2049M \
    -drive file=$BUILDROOT_PATH/output/images/rootfs.ext4,format=raw \
    -append "root=/dev/sda rw console=ttyS0,115200 acpi=off nokaslr" \
    -serial stdio \
    -display none \
    -s -S
```

- `-s`: Opens a GDB server on port 1234.
- `-S`: Stops QEMU execution, allowing GDB to connect.

# Debugging with gdb-multiarch

## Installing:

```bash
sudo apt-get install gdb-multiarch
```

Add the following line to your `~/.gdbinit` file to load the GDB scripts provided by the kernel for enhanced debugging:

```bash
add-auto-load-safe-path <replace_kernel_path>/scripts/gdb/vmlinux-gdb.py
```

This enables GDB helper scripts that are useful for kernel debugging.

## Debugging Session:

### Start QEMU in Debug Mode

Ensure QEMU is running with the -s -S options so that it waits for GDB to connect.

### Lauch GDB

In another terminal, start gdb-multiarch and load the kernel symbols from vmlinux:

```bash
gdb-multiarch vmlinux
```

In GDB, connect to QEMU by running `target remote :1234`:

```bash
(gdb) target remote :1234
Remote debugging using :1234
0x000000000000fff0 in exception_stacks ()
```

Now you can debug the kernel:

```bash
(gdb) hb start_kernel
Hardware assisted breakpoint 1 at 0xffffffff834174c3: file init/main.c, line 905.
(gdb) c
Continuing.

Breakpoint 1, start_kernel () at init/main.c:905
905		char *command_line;
```

# References

- https://medium.com/@depressedcoder/m1-mac-linux-kernel-development-environment-setup-748637131f92