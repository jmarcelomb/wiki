

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | \
  sh -s -- install
```
You will need to explicitly say no when prompted to install Determinate Nix

```bash
nix run nix-darwin/master#darwin-rebuild -- switch --flake .#mac-mini
```