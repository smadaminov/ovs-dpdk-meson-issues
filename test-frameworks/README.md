# Instructions and Demos

## bandit

Specifically target C++ application, however, looks like it could be possible to
test C programs. It needs C++11 features supported by the compiler, but there is
another framework Igloo (https://iglootesting.wordpress.com/) that does not
require them. So looks like a potential candidate so far.

## Catch2

Seems to be similar to `bandit`. `Catch2` also targets C++ and says that C may
work. Though it looks off-putting that it was stated in a such way. So far
`bandit` looks more promising that `Catch2` because of that.

## Criterion

Among nice features it has support for test suites and fixtures.

### RHEL8

First, you need to install `meson` and `ninja` to build Criterion from sources.
Then, install `cmake` as it is required to build a `nanomsg` subproject:

```sh
sudo dnf install cmake
```

Now let's build Criterion:

```sh
git clone --recursive https://github.com/Snaipe/Criterion
cd Criterion
meson build
ninja -C build
```

However, the last step failed with an error message:

```sh
FAILED: subprojects/libffi/src/libffi.so.7.1.0.p/x86_unix64.S.o
cc -Isubprojects/libffi/src/libffi.so.7.1.0.p -Isubprojects/libffi/src -I../subprojects/libffi/src -Isubprojects/libffi -I../subprojects/libffi -Isubprojects/libffi/include -I../subprojects/libffi/include -fdiagnostics-color=always -D_FILE_OFFSET_BITS=64 -Wall -Winvalid-pch -std=c11 -g -DFFI_BUILDING -fPIC -DTARGET=X86_64 -MD -MQ subprojects/libffi/src/libffi.so.7.1.0.p/x86_unix64.S.o -MF subprojects/libffi/src/libffi.so.7.1.0.p/x86_unix64.S.o.d -o subprojects/libffi/src/libffi.so.7.1.0.p/x86_unix64.S.o -c ../subprojects/libffi/src/x86/unix64.S
../subprojects/libffi/src/x86/unix64.S: Assembler messages:
../subprojects/libffi/src/x86/unix64.S:451: Error: junk at end of line, first unrecognized character is `@'
../subprojects/libffi/src/x86/unix64.S:470: Error: junk at end of line, first unrecognized character is `@'
../subprojects/libffi/src/x86/unix64.S:483: Error: junk at end of line, first unrecognized character is `@'
../subprojects/libffi/src/x86/unix64.S:497: Error: junk at end of line, first unrecognized character is `@'
../subprojects/libffi/src/x86/unix64.S:510: Error: junk at end of line, first unrecognized character is `@'
```

Thus, we stopped here as we want the test framework to work out-of-the-box on
all platforms of interest.

## UNITY

Targets embedded microcontrollers and overall it is specifically a unit testing
framework for C. It lacks features such as capturing the stdout of SUT and not
clear how to test TAB completion with it. So we pass on this framework too.

## License

BSD 3-Clause
