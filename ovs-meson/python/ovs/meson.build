# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

conf_dirs_py = configuration_data()
conf_dirs_py.set('LOGDIR', '/var/log/openvswitch')
conf_dirs_py.set('RUNDIR', '/var/run/openvswitch')
conf_dirs_py.set('DBDIR', '/etc/openvswitch')
conf_dirs_py.set('bindir', '/bin')
conf_dirs_py.set('pkgdatadir', '/usr/share/openvswitch')
conf_dirs_py.set('variables', '@variables@')

configure_file(
    input : meson.project_source_root() + '/python/ovs/dirs.py.template',
    output : 'dirs.py',
    configuration : conf_dirs_py,
)

python_ovs_dirs_py = run_command(
    prog_python,
    meson.project_source_root() + '/build-aux/copy-file-from-build.py',
    'dirs.py',
    'dirs.py',
    check : true,
)
