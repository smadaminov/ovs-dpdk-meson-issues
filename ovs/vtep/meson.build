# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

sources = files(
    'vtep-idl.c',
)

deps = []

mapfile = meson.project_build_root() + '/vtep.map'
vflag = '-Wl'.format(meson.current_source_dir(), mapfile)
vtep = library(
  'vtep', sources,
  dependencies : deps,
  include_directories : global_inc,
  link_args : ['-Wl,--no-undefined', vflag],
  link_depends : mapfile,
  version : as_version,
  soversion : as_soversion,
)

sources = files(
    'vtep-ctl.c',
)

deps = []

executable('vtep-ctl', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined'],
    link_with : [ vtep, openvswitch ],
)
