# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

# MSR: in this form it is not portable!
include_odp_netlink_h = custom_target(
    'odp-netlink.h',
    input : meson.project_source_root() + '/datapath/linux/compat/include/linux/openvswitch.h',
    output : 'odp-netlink.h',
    command : [
        'sed',
        '-f',
        meson.project_source_root() + '/build-aux/extract-odp-netlink-h',
    ],
    feed : '@INPUT@',
    capture : '@OUTPUT@',
)

# MSR: in this form it is not portable!
include_odp_netlink_macros_h = custom_target(
    'odp-netlink-macros.h',
    input : include_odp_netlink_h,
    output : 'odp-netlink-macros.h',
    command : [
        'sh',
        '-f',
        meson.project_source_root() + '/build-aux/extract-odp-netlink-macros-h',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
)

subdir('openvswitch')
