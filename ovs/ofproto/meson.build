# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

ofproto_ipfix_entities_def = custom_target(
    'ipfix-entities.def',
    input : meson.project_source_root() + '/ofproto/ipfix.xml',
    output : 'ipfix-entities.def',
    command : [
        prog_python,
        meson.project_source_root() + '/ofproto/ipfix-gen-entities',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : [
        'PYTHONPATH=' + meson.project_source_root() + '/python' + ':' + meson.project_build_root() + '/python',
#        'PYTHONPATH=' + meson.project_source_root() + '/python',
        'PYTHONDONTWRITEBYTECODE=yes', # this prevents creation of *.pyc files in 'python/build/__pycache__' directory
    ],
)

sources = files(
	'bond.c',
	'collectors.c',
	'connmgr.c',
	'fail-open.c',
	'in-band.c',
	'names.c',
	'netflow.c',
	'ofproto.c',
	'ofproto-dpif.c',
	'ofproto-dpif-ipfix.c',
	'ofproto-dpif-mirror.c',
	'ofproto-dpif-monitor.c',
	'ofproto-dpif-rid.c',
	'ofproto-dpif-sflow.c',
	'ofproto-dpif-trace.c',
	'ofproto-dpif-upcall.c',
	'ofproto-dpif-xlate.c',
	'ofproto-dpif-xlate-cache.c',
	'pinsched.c',
	'tunnel.c',
	'bundles.c',
)

sources += [
    include_odp_netlink_h,
    ofproto_ipfix_entities_def,
]

deps = []

mapfile = meson.project_build_root() + '/ofproto.map'
vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
ofproto = library(
  'ofproto', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined', vflag],
  link_depends : mapfile,
  link_with : sflow,
  version : as_version,
  soversion : as_soversion,
)
