# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

# ovsdb/_server.ovsschema.inc
ovsdb__server_ovsschema_inc = custom_target(
    '_server.ovsschema.inc',
    input : meson.project_source_root() + '/ovsdb/_server.ovsschema',
    output : '_server.ovsschema.inc',
    command : [
        prog_python,
        meson.project_source_root() + '/build-aux/text2c',
    ],
    feed : true,
    capture : '@OUTPUT@',
    env : python_env,
)

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

mapfile = meson.project_build_root() + '/ovsdb.map'
vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
ovsdb = library(
  'ovsdb', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined', vflag],
  link_depends : mapfile,
  version : as_version,
  soversion : as_soversion,
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

sources += [
    ovsdb__server_ovsschema_inc,
]

deps = []

executable('ovsdb-server', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined'],
    link_with : [ ovsdb, openvswitch ],
    install : true,
    install_dir: install_prefix / 'sbin',
)
