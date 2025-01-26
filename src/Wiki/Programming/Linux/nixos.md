# NixOS

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

```
home-manager build --flake .
```

