How can we performe a `cargo update` for the `cargo install` command?

There is no such command in vanilla cargo (well, there's cargo install but that's for dependencies), but since cargo supports third-party subcommands there is an answer: the [`cargo-update`](https://github.com/nabijaczleweli/cargo-update) [crate](https://crates.io/crates/cargo-update).

Install as usual with:
```bash
cargo install cargo-update
```

then use

```bash
cargo install-update -a
```

To update all installed packages, for more usage information and examples see the cargo `install-update` man page.

