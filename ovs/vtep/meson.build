# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

vtep_vtep_idl_c = custom_target(
    'vtep-idl.c',
#    input : meson.project_source_root() + '/vtep/vtep-idl.ovsidl',
    input : vtep_vtep_idl_ovsidl,
    output : 'vtep-idl.c',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'c-idl-source',
        '@INPUT@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

vtep_vtep_idl_h = custom_target(
    'vtep-idl.h',
#    input : meson.project_source_root() + '/vtep/vtep-idl.ovsidl',
    input : vtep_vtep_idl_ovsidl,
    output : 'vtep-idl.h',
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
#    'vtep-idl.c',
#)
sources = [
    vtep_vtep_idl_c,
    vtep_vtep_idl_h,
]

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

sources += [
    vtep_vtep_idl_h,
]

deps = []

executable('vtep-ctl', sources,
    dependencies : deps,
    include_directories : global_inc,
    link_args : ['-Wl,--no-undefined'],
    link_with : [ vtep, openvswitch ],
)
