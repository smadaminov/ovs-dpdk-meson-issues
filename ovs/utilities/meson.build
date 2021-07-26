# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

sources = files(
    'ovs-appctl.c',
)

deps = []

executable('ovs-appctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
)

sources = files(
    'ovs-testcontroller.c',
)

deps = [ m_dep ]

executable('ovs-testcontroller', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
)

sources = files(
    'ovs-dpctl.c',
)

deps = [ m_dep ]

executable('ovs-dpctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
)

sources = files(
    'ovs-ofctl.c',
)

deps = [ m_dep ]

executable('ovs-ofctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : [ openvswitch, ofproto ],
)

sources = files(
    'ovs-vsctl.c',
)

deps = [ m_dep ]

executable('ovs-vsctl', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : openvswitch,
)
