# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

sources = files(
    'bridge.c',
    'ovs-vswitchd.c',
    'system-stats.c',
    'xenserver.c',
)

sources += [
	include_odp_netlink_h,
]

sources += lib_vswitch_idl_h

deps = []

if build_machine.system() == 'linux'
    deps += m_dep
endif

executable('ovs-vswitchd', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : [ openvswitch, ofproto, sflow ],
  install : true,
  install_dir: install_prefix / 'sbin',
)
