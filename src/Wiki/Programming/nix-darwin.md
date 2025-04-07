How to install `nix` to use in `nix-darwin`:

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | \
  sh -s -- install
```
You will need to explicitly say no when prompted to install Determinate Nix

How to install homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

How to run nix-darwin:

```bash
nix run nix-darwin/master#darwin-rebuild -- switch --flake .#mac-mini
```