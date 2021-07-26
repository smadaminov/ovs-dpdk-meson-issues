# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

sources = files(
	'column.c',
	'condition.c',
	'execution.c',
	'file.c',
	'jsonrpc-server.c',
	'log.c',
	'mutation.c',
	'ovsdb.c',
	'monitor.c',
	'query.c',
	'raft.c',
	'raft-private.c',
	'raft-rpc.c',
	'rbac.c',
	'replication.c',
	'relay.c',
	'row.c',
	'server.c',
	'storage.c',
	'table.c',
	'trigger.c',
	'transaction.c',
	'transaction-forward.c',
	'ovsdb-util.c',
)

deps = []

mapfile = 'ovsdb.map'
vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
ovsdb = static_library(
  'ovsdb', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined', vflag],
  link_depends : mapfile,
)

sources = files(
    'ovsdb-tool.c',
)

deps = []

executable('ovsdb-tool', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined'],
    link_with : [ ovsdb, openvswitch ],
    install : true,
    install_dir: install_prefix / 'bin',
)

sources = files(
    'ovsdb-client.c',
)

deps = []

executable('ovsdb-client', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined'],
    link_with : [ ovsdb, openvswitch ],
    install : true,
    install_dir: install_prefix / 'bin',
)

sources = files(
    'ovsdb-server.c',
)

deps = []

executable('ovsdb-server', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined'],
    link_with : [ ovsdb, openvswitch ],
    install : true,
    install_dir: install_prefix / 'sbin',
)
