Porting OvS-DPDK to Windows with Meson
--------------------------------------

For the OvS kernel driver for Windows you may need to `enable`_ test signing.
Also, make sure that you have installed `Spectre-mitigated`_ libraries.

.. _enable:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/6

.. _Spectre-mitigated:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/7

Known Issues
************

- `A WDK corresponding to target version '10.0.19041.0' was not found. Please install this WDK version before building`_

- `error: possibly undefined macro: LT_INIT`_

- `ImportError: DLL load failed while importing win32file: The specified procedure could not be found`_

- `LNK2019: unresolved external symbol __stdio_common_vswprintf`_

- `'MakeCert' is not recognized as an internal or external command, operable program or batch file`_

- `ModuleNotFoundError: No module named 'ntsecuritycon'`_

- `Package dpdk was not found in the pkg-config search path`_

- `SIGNTASK : SignTool warning : No file digest algorithm specified`_

- `x86_64-w64-mingw32-ar not found`_


.. _A WDK corresponding to target version '10.0.19041.0' was not found. Please install this WDK version before building:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/4

.. _error\: possibly undefined macro\: LT_INIT:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/57

.. _ImportError\: DLL load failed while importing win32file\: The specified procedure could not be found:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/63

.. _LNK2019\: unresolved external symbol __stdio_common_vswprintf:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/1

.. _'MakeCert' is not recognized as an internal or external command, operable program or batch file:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/2

.. _ModuleNotFoundError\: No module named 'ntsecuritycon':
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/44

.. _Package dpdk was not found in the pkg-config search path:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/38

.. _SIGNTASK \: SignTool warning \: No file digest algorithm specified:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/9

.. _x86_64-w64-mingw32-ar not found:
    https://github.com/smadaminov/ovs-dpdk-meson-issues/issues/5

Useful Links
************

DPDK kmods
git://dpdk.org/dpdk-kmods
