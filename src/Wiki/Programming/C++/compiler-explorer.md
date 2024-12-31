# Compiler Explorer

C++ for cortex m0+ flags:

```
	-mthumb -mcpu=cortex-m0plus -mfloat-abi=soft
```

Other falgs:

```
	-O3 -Wall -Wextra -Wpedantic -Wshadow
```
[ffunction-sections, -fdata-sections, & --gc-sections](https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#-ffunction-sections--fdata-sections----gc-sections)

`-fno-exceptions`

`-O3 -Wall -Wextra -Wpedantic -Wshadow -mthumb -mcpu=cortex-m0plus -mfloat-abi=soft -fdata-sections -ffunction-sections -fno-exceptions -fno-rtti`

Exception handling and RTTI are difficult to provide without dynamic memory allocation (much more on that below), so you likely want to disable them with `fno-exceptions`, `fno-non-call-exceptions`, and `fno-rtti`.