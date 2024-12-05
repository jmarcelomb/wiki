# Using tailscale in LXC containers

The contents of the this page serve mostly as a note-to-self for the future and are sourced from tailscale's [documentation](https://tailscale.com/kb/1130/lxc-unprivileged).

## What

I have a few LXC containers on proxmox where I want to run tailscale. After installing tailscale, doing `tailscale up` throws an error telling me to do `sudo systemctl start tailscaled`.

## Why

By default, when you create an LXC contained in proxmox it lacks the privileges to access the networking resource needed for tailscale to work.

## How

To fix this, we need to give the container the privileges it requires. Example with a container with ID 104:

- Start a shell on the Proxmox host
- Open the `/etc/pve/lxc/104.conf` file with whatever text editor
- Add the following two lines at the end and save the file:

```sh
lxc.cgroup2.devices.allow: c 10:200 rwm
lxc.mount.entry: /dev/net/tun dev/net/tun none bind,create=file
