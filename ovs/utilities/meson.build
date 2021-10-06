# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

sources = files(
    'ovs-appctl.c',
)

deps = []
if enable_dpdk
    deps += dpdk_lib_deps
endif

executable('ovs-appctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
  install : true,
  install_dir: install_prefix / 'bin',
)

sources = files(
    'ovs-testcontroller.c',
)

if build_machine.system() == 'linux'
    deps += m_dep
endif

executable('ovs-testcontroller', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
  install : true,
  install_dir: install_prefix / 'bin',
)

sources = files(
    'ovs-dpctl.c',
)

sources += [
	include_odp_netlink_h,
]

executable('ovs-dpctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
  install : true,
  install_dir: install_prefix / 'bin',
)

sources = files(
    'ovs-ofctl.c',
)

sources += [
	include_odp_netlink_h,
]

executable('ovs-ofctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : [ openvswitch, ofproto ],
  install : true,
  install_dir: install_prefix / 'bin',
)

sources = files(
    'ovs-vsctl.c',
)

sources += lib_vswitch_idl_h

executable('ovs-vsctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
  install : true,
  install_dir: install_prefix / 'bin',
)
