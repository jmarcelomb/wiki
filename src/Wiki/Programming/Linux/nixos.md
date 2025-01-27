# NixOS

## nixos-rebuild:

```sh
nixos-rebuild build --flake .#name
```

Switch:

```sh
nixos-rebuild switch --flake .#name
```

## nix-shell

Example of setup shell with git and pre-commit:

```sh
nix-shell -p git pre-commit
```

## Enable flakes permanently in NixOS
Add the following to the system configuration (flakes):

```nix
  nix.settings.experimental-features = [ "nix-command" "flakes" ];
```

## Enable vmware guest

```nix
    virtualisation.vmware.guest.enable = true;
```

## Home manager

Build:

```
home-manager build --flake .
```

Switch:

```
home-manager switch --flake .
```

## Clean up

If you do the last command you should be able to clean it out for the boot

```sh
nix-env --list-generations

nix-collect-garbage  --delete-old

nix-collect-garbage  --delete-generations 1 2 3

# recommeneded to sometimes run as sudo to collect additional garbage
sudo nix-collect-garbage -d

# As a separation of concerns - you will need to run this command to clean out boot
sudo /run/current-system/bin/switch-to-configuration boot
```