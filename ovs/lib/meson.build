# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

lib_ovsdb_server_idl_c = custom_target(
    'ovsdb-server-idl.c',
#    input : meson.project_source_root() + '/lib/ovsdb-server-idl.ovsidl',
    input : lib_ovsdb_server_idl_ovsidl,
    output : 'ovsdb-server-idl.c',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'c-idl-source',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

lib_ovsdb_server_idl_h = custom_target(
    'ovsdb-server-idl.h',
#    input : meson.project_source_root() + '/lib/ovsdb-server-idl.ovsidl',
    input : lib_ovsdb_server_idl_ovsidl,
    output : 'ovsdb-server-idl.h',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'c-idl-header',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

lib_vswitch_idl_c = custom_target(
    'vswitch-idl.c',
#    input : meson.project_source_root() + '/lib/vswitch-idl.ovsidl',
    input : lib_vswitch_idl_ovsidl,
    output : 'vswitch-idl.c',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'c-idl-source',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

lib_vswitch_idl_h = custom_target(
    'vswitch-idl.h',
#    input : meson.project_source_root() + '/lib/vswitch-idl.ovsidl',
    input : lib_vswitch_idl_ovsidl,
    output : 'vswitch-idl.h',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'c-idl-header',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

#sources = files(
#    'dpif-netdev-lookup-avx512-gather.c',
#    'dpif-netdev-extract-avx512.c',
#    'dpif-netdev-avx512.c',
#)
#
#deps = []
#
#mapfile = '../openvswitchavx512.map'
#vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
#openvswitchavx512 = library(
#  'openvswitchavx512', sources,
#  dependencies : deps,
#  include_directories : global_inc,
#  c_args : [
#    '-mavx512f',
#    '-mavx512bw',
#    '-mavx512dq',
#    '-mbmi',
#    '-mbmi2',
#    '-fPIC',
#  ],
#  link_args : ['-Wl,--no-undefined', vflag],
#  link_depends : mapfile,
#  version : as_version,
#  soversion : as_soversion,
#)
#

sources = files(
    'sflow_agent.c',
    'sflow_sampler.c',
    'sflow_poller.c',
    'sflow_receiver.c',
)

deps = []

mapfile = meson.project_build_root() + '/sflow.map'
vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
sflow = library(
  'sflow', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined', vflag],
  link_depends : mapfile,
  version : as_version,
  soversion : as_soversion,
)

# MSR: file generation probably should be moved to a separate folder with its own meson.build file
# lib/meta-flow.inc
lib_meta_flow_inc = custom_target(
    'meta-flow.inc',
    input : meson.project_source_root() + '/include/openvswitch/meta-flow.h',
    output : 'meta-flow.inc',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-ofp-fields',
        'meta-flow',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

# lib/nx-match.inc
lib_nx_match_inc = custom_target(
    'nx-match.inc',
    input : meson.project_source_root() + '/include/openvswitch/meta-flow.h',
    output : 'nx-match.inc',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-ofp-fields',
        'nx-match',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

# lib/ofc-actions.inc1
lib_ofp_actions_inc1 = custom_target(
    'ofp-actions.inc1',
    input : meson.project_source_root() + '/lib/ofp-actions.c',
    output : 'ofp-actions.inc1',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-ofp-actions',
        'prototypes',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

# lib/ofc-actions.inc2
lib_ofp_actions_inc2 = custom_target(
    'ofp-actions.inc2',
    input : meson.project_source_root() + '/lib/ofp-actions.c',
    output : 'ofp-actions.inc2',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-ofp-actions',
        'definitions',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

# lib/ofp-errors.inc
lib_ofp_errors_inc = custom_target(
    'ofp-errors.inc',
    input : [
        meson.project_source_root() + '/include/openvswitch/ofp-errors.h',
        meson.project_source_root() + '/include/openflow/openflow-common.h',
    ],
    output : 'ofp-errors.inc',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-ofp-errors',
        '@INPUT0@',
        '@INPUT1@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

# lib/ofp-msgs.inc
lib_ofp_msgs_inc = custom_target(
    'ofp-msgs.inc',
    input : [
        meson.project_source_root() + '/include/openvswitch/ofp-msgs.h',
    ],
    output : 'ofp-msgs.inc',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/extract-ofp-msgs',
        '@INPUT@',
        'lib/ofp-msgs.inc',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

sources = files(
	'aes128.c',
	'backtrace.c',
	'bfd.c',
	'bundle.c',
	'byteq.c',
	'cfm.c',
	'classifier.c',
	'ccmap.c',
	'cmap.c',
	'colors.c',
	'command-line.c',
	'connectivity.c',
	'conntrack-icmp.c',
	'conntrack-tcp.c',
	'conntrack-tp.c',
	'conntrack-other.c',
	'conntrack.c',
	'coverage.c',
	'crc32c.c',
	'csum.c',
	'ct-dpif.c',
	'daemon.c',
	'db-ctl-base.c',
	'dummy.c',
	'dpctl.c',
	'dp-packet.c',
	'dpif-netdev-extract-study.c',
	'dpif-netdev-lookup.c',
	'dpif-netdev-lookup-autovalidator.c',
	'dpif-netdev-lookup-generic.c',
	'dpif-netdev.c',
	'dpif-netdev-private-dfc.c',
	'dpif-netdev-private-dpif.c',
	'dpif-netdev-private-extract.c',
	'dpif-netdev-perf.c',
	'dpif.c',
	'heap.c',
	'dynamic-string.c',
	'entropy.c',
	'fat-rwlock.c',
	'fatal-signal.c',
	'flow.c',
	'guarded-list.c',
	'hash.c',
	'hindex.c',
	'hmap.c',
	'hmapx.c',
	'id-pool.c',
	'if-notifier-manual.c',
	'ipf.c',
	'jhash.c',
	'json.c',
	'jsonrpc.c',
	'lacp.c',
	'learn.c',
	'learning-switch.c',
	'lockfile.c',
	'mac-learning.c',
	'match.c',
	'mcast-snooping.c',
	'memory.c',
	'meta-flow.c',
	'multipath.c',
	'namemap.c',
	'netdev-dummy.c',
	'netdev-offload.c',
	'netdev-vport.c',
	'netdev.c',
	'netlink.c',
	'nx-match.c',
	'object-collection.c',
	'odp-execute.c',
	'odp-util.c',
	'ofp-actions.c',
	'ofp-bundle.c',
	'ofp-connection.c',
	'ofp-ed-props.c',
	'ofp-errors.c',
	'ofp-flow.c',
	'ofp-group.c',
	'ofp-ipfix.c',
	'ofp-match.c',
	'ofp-meter.c',
	'ofp-monitor.c',
	'ofp-msgs.c',
	'ofp-packet.c',
	'ofp-parse.c',
	'ofp-port.c',
	'ofp-print.c',
	'ofp-prop.c',
	'ofp-protocol.c',
	'ofp-queue.c',
	'ofp-switch.c',
	'ofp-table.c',
	'ofp-util.c',
	'ofp-version-opt.c',
	'ofpbuf.c',
	'ovs-atomic-locked.c',
	'ovs-lldp.c',
	'ovs-numa.c',
	'ovs-rcu.c',
	'ovs-replay.c',
	'ovs-router.c',
	'ovs-thread.c',
	'ovsdb-cs.c',
	'ovsdb-data.c',
	'ovsdb-error.c',
	'ovsdb-idl.c',
	'ovsdb-map-op.c',
	'ovsdb-set-op.c',
	'ovsdb-condition.c',
	'ovsdb-parser.c',
	'ovsdb-session.c',
	'ovsdb-types.c',
	'ox-stat.c',
	'packets.c',
	'pcap-file.c',
	'perf-counter.c',
	'stopwatch.c',
	'poll-loop.c',
	'process.c',
	'pvector.c',
	'random.c',
	'rconn.c',
	'reconnect.c',
	'rstp.c',
	'rstp-state-machines.c',
	'seq.c',
	'sha1.c',
	'shash.c',
	'simap.c',
	'skiplist.c',
	'smap.c',
	'socket-util.c',
	'sort.c',
	'sset.c',
	'stp.c',
	'stream-fd.c',
	'stream-replay.c',
	'stream-tcp.c',
	'stream.c',
	'stdio.c',
	'string.c',
	'svec.c',
	'syslog-direct.c',
	'syslog-libc.c',
	'syslog-null.c',
	'table.c',
	'timer.c',
	'timeval.c',
	'tnl-neigh-cache.c',
	'tnl-ports.c',
	'netdev-native-tnl.c',
	'token-bucket.c',
	'tun-metadata.c',
	'unicode.c',
	'unixctl.c',
	'userspace-tso.c',
	'util.c',
	'uuid.c',
	'vconn-stream.c',
	'vconn.c',
	'vlan-bitmap.c',
	'vlog.c',
	'lldp/lldp.c',
	'lldp/lldpd.c',
	'lldp/lldpd-structs.c',
	'dpdk-stub.c',
    'async-append-null.c', # no POSIX_AIO
    'stream-nossl.c',
    'dns-resolve.h',
    'dns-resolve-stub.c',
)

if build_machine.system() == 'windows'
    sources += files(
        'daemon-windows.c',
        'getopt_long.c',
        'getrusage-windows.c',
        'latch-windows.c',
        'route-table-stub.c',
        'if-notifier-stub.c',
        'stream-windows.c',
        'strsep.c',
        'dpif-netlink.c',
        'netdev-windows.c',
        'netlink-conntrack.c',
        'netlink-notifier.c',
        'netlink-socket.c',
        'wmi.c',
    )
endif

if build_machine.system() == 'linux'
    sources += files(
        'daemon-unix.c',
        'latch-unix.c',
        'signals.c',
        'socket-util-unix.c',
        'stream-unix.c',
        'dpif-netlink.c',
        'dpif-netlink-rtnl.c',
        'if-notifier.c',
        'netdev-linux.c',
        'netdev-offload-tc.c',
        'netlink-conntrack.c',
        'netlink-notifier.c',
        'netlink-socket.c',
        'rtnetlink.c',
        'route-table.c',
        'tc.c',
    )
endif

sources += [
    meson.project_build_root() + '/' + 'dirs.c',
    lib_ovsdb_server_idl_c,
    lib_ovsdb_server_idl_h,
    lib_vswitch_idl_c,
    lib_vswitch_idl_h,
    include_odp_netlink_h,
    include_odp_netlink_macros_h,
]

sources += [
    lib_meta_flow_inc,
    lib_nx_match_inc,
    lib_ofp_actions_inc1,
    lib_ofp_actions_inc2,
    lib_ofp_errors_inc,
    lib_ofp_msgs_inc,
]

deps = [ thread_dep ]

mapfile = meson.project_build_root() + '/openvswitch.map'
vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
openvswitch = library(
    'openvswitch', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined', vflag],
    link_depends : mapfile,
#    link_with : openvswitchavx512,
    version : as_version,
    soversion : as_soversion,
)

#global_libs += openvswitchavx512
global_libs += sflow
global_libs += openvswitch
