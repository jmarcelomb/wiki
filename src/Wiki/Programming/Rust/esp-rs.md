## How to flash and monitor:

```sh
espflash flash --monitor target/riscv32imc-unknown-none-elf/debug/test-esp3
```

Or use `cargo run` by adding to `.cargo/` the file `config.toml` the following:

```toml
[target.riscv32imc-unknown-none-elf]
runner = "espflash flash --monitor"
```

An example of my fool `config.toml` is:

```toml
[target.riscv32imc-unknown-none-elf]
runner = "espflash flash --monitor"

[env]
ESP_LOG="INFO"

[build]
rustflags = [
  # Required to obtain backtraces (e.g. when using the "esp-backtrace" crate.)
  # NOTE: May negatively impact performance of produced code
  "-C", "force-frame-pointers",
]

target = "riscv32imc-unknown-none-elf"

[unstable]
build-std = ["core"]
```