# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

m_dep = cc.find_library('m', required : true)

sources = files(
    'bridge.c',
    'ovs-vswitchd.c',
    'system-stats.c',
    'xenserver.c',
)

deps = [ m_dep ]

executable('ovs-vswitchd', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined'],
  link_with : [ openvswitch, ofproto, sflow ],
)
