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

# NixGL

All the programs I have that require gpu acceleration have a module option for it, but I suppose if it doesnt, you could always just wrap the program with a script that runs it with nixGL for you XD Something like the below, then put someprogram in your packages list instead of the actual package

```nix
someprogram = pkgs.writeShellScriptBin "someprogram" ''
${nixGL} ${pkgs.someprogram}/bin/someprogram "$@"'';
```