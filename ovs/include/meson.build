# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

include_odp_netlink_h = custom_target(
    'odp-netlink.h',
    input : meson.project_source_root() + '/datapath/linux/compat/include/linux/openvswitch.h',
    output : 'odp-netlink.h',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-odp-netlink-h.py',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

include_odp_netlink_macros_h = custom_target(
    'odp-netlink-macros.h',
    input : include_odp_netlink_h,
    output : 'odp-netlink-macros.h',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-odp-netlink-macros-h.py',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

subdir('openvswitch')
