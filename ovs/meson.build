# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

# Meson Newer Version Justification
# Version 0.56.0: enables 'project_build_root' for 'meson' object
# Version 0.57.0: enables use of 'env' in 'custom_target'
# Version 0.59.0: enables use of 'feed' in 'custom_target'

project('openvswitch', 'C',
        version: '2.16.90',
        license: 'Apache2.0',
        default_options: ['buildtype=release', 'default_library=static'],
        meson_version: '>= 0.59.0'
)

as_version = meson.project_version()
ver_arr = as_version.split('.')

as_current_version  = ver_arr[0]
as_revision_version = ver_arr[1]
as_age_version      = ver_arr[2]

as_soversion = '0'
conf_soversion = configuration_data()
conf_soversion.set('SOVERSION', as_soversion)

cc = meson.get_compiler('c')

prog_python = import('python').find_installation('python3')
python_env = environment()
python_env.set('PYTHONPATH', meson.project_source_root() + '/python')
# Prevent creation of *.pyc files in 'python/build/__pycache__' directory
python_env.set('PYTHONDONTWRITEBYTECODE', 'yes')
cdata = configuration_data()

if build_machine.system() == 'linux'
    m_dep = cc.find_library('m', required : true)
    thread_dep = dependency('threads', required : true)
endif

# MSR: path for pthreads DLL should be collected
# from options and not hardcoded
if build_machine.system() == 'windows'
    thread_dep = cc.find_library(
        'pthreadVC3-w32',
        dirs : [
            'C:/pthreads/pthreads4w',
        ],
        required : true,
    )
    # Resolve symbols for Winsock
    Ws2_32_dep = cc.find_library(
        'Ws2_32',
        required : true,
    )
    WbemUuid_dep = cc.find_library(
        'WbemUuid',
    required : true,
    )
    Shlwapi_dep = cc.find_library(
        'Shlwapi',
        required : true,
    )
    Iphlpapi_dep = cc.find_library(
        'Iphlpapi',
        required : true,
    )
endif

check_headers = [
  ['HAVE_BITS_FLOATN_COMMON_H', 'bits/floatn/common.h'],
  ['HAVE_DLFCN_H', 'dlfcn.h'],
  ['HAVE_INTTYPES_H', 'inttypes.h'],
  ['HAVE_LIBUNWIND_H', 'libunwind.h'],
  ['HAVE_LINUX_IF_ETHER_H', 'linux/if/ether.h'],
  ['HAVE_LINUX_NET_NAMESPACE_H', 'linux/net/namespace.h'],
  ['HAVE_LINUX_PERF_EVENT_H', 'linux/perf/event.h'],
  ['HAVE_LINUX_TYPES_H', 'linux/types.h'],
  ['HAVE_MEMORY_H', 'memory.h'],
  ['HAVE_MNTENT_H', 'mntent.h'],
  ['HAVE_NET_IF_MIB_H', 'net/if/mib.h'],
  ['HAVE_NETLINK', 'linux/netlink.h'],
  ['HAVE_RTE_CONFIG_H', 'rte/config.h'],
  ['HAVE_STDATOMIC_H', 'stdatomic.h'],
  ['HAVE_STDINT_H', 'stdint.h'],
  ['HAVE_STDIO_H', 'stdio.h'],
  ['HAVE_STDLIB_H', 'stdlib.h'],
  ['HAVE_STRINGS_H', 'strings.h'],
  ['HAVE_STRING_H', 'string.h'],
  ['HAVE_SYS_STATVFS_H', 'sys/statvfs.h'],
  ['HAVE_SYS_STAT_H', 'sys/stat.h'],
  ['HAVE_SYS_TYPES_H', 'sys/types.h'],
  ['HAVE_UNISTD_H', 'unistd.h'],
  ['HAVE_VALGRIND_VALGRIND_H', 'valgrind/valgrind.h'],
]

foreach h : check_headers
  if cc.has_header(h.get(1))
    cdata.set(h.get(0), 1)
  endif
endforeach

check_functions = [
# check token ['HAVE_AF_XDP']
# check token ['HAVE_ATOMIC']
# check token ['HAVE_BACKTRACE']
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include<time.h>', []],
# check token ['HAVE_CXX11']
# check token ['HAVE_DECL_MALLOC_TRIM']
# check token ['HAVE_DECL_RTE_EAL_NUMA_AWARE_HUGEPAGES']
# check token ['HAVE_DECL_RTE_LIBRTE_VHOST_NUMA']
# check token ['HAVE_DECL_STRERROR_R']
# check token ['HAVE_DECL_SYS_SIGLIST']
# check token ['HAVE_GCC4_ATOMICS']
  ['HAVE_GETLOADAVG', 'getloadavg', '#include<stdlib.h>', []],
  ['HAVE_GETMNTENT_R', 'getmntent_r', '#include<mntent.h>', []],
# check token ['HAVE_GLIBC_PTHREAD_SETNAME_NP']
# check token ['HAVE_IF_DL']
# check token ['HAVE_LIBCAPNG']
# check token ['HAVE_LIBSOCKET']
# check token ['HAVE_MLOCKALL']
# check token ['HAVE_NETBSD_PTHREAD_SETNAME_NP']
# check token ['HAVE_NETLINK']
# check token ['HAVE_NLA_BITFIELD32']
# check token ['HAVE_OPENSSL']
  ['HAVE_POSIX_MEMALIGN', 'posix_memalign', '#include<stdlib.h>', []],
# check token ['HAVE_PRAGMA_MESSAGE']
  ['HAVE_PTHREAD_SET_NAME_NP', 'pthread_set_name_np', '#include<pthread.h>', []],
# check token ['HAVE_PTHREAD_SPIN_LOCK']
# check token ['HAVE_SCTP_CONNTRACK_HEARTBEATS']
  ['HAVE_SENDMMSG', 'sendmmsg', '#include<sys/socket.h>', ['-D_GNU_SOURCE']],
  ['HAVE_STATVFS', 'statvfs', '#include<sys/statvfs.h>', []],
  ['HAVE_STRERROR_R', 'strerror_r', '#include<string.h>', []],
# check token ['HAVE_STRNLEN']
# check token ['HAVE_STRTOK_R_BUG']
# check token ['HAVE_STRUCT_IFREQ_IFR_FLAGSHIGH']
# check token ['HAVE_STRUCT_SOCKADDR_IN6_SIN6_SCOPE_ID']
# check token ['HAVE_STRUCT_STAT_ST_MTIMENSEC']
# check token ['HAVE_STRUCT_STAT_ST_MTIM_TV_NSEC']
# check token ['HAVE_STRUCT_TCF_T_FIRSTUSE']
# check token ['HAVE_STRUCT_TIMESPEC']
# check token ['HAVE_TCA_MPLS_TTL']
# check token ['HAVE_TCA_PEDIT_KEY_EX_HDR_TYPE_UDP']
# check token ['HAVE_TCA_POLICE_PKTRATE64']
# check token ['HAVE_TCA_SKBEDIT_FLAGS']
# check token ['HAVE_TCA_TUNNEL_KEY_ENC_TTL']
# check token ['HAVE_TCA_VLAN_PUSH_VLAN_PRIORITY']
# check token ['HAVE_THREAD_LOCAL']
# check token ['HAVE_UNBOUND']
# check token ['HAVE_UNWIND']
# check token ['HAVE_VIRTIO_TYPES']
# check token ['HAVE_XDP_NEED_WAKEUP']
# check token ['HAVE___THREAD']
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2), args : f.get(3))
    cdata.set(f.get(0), 1)
  endif
endforeach

check_structs = [
  ['HAVE_NLA_BITFIELD32', 'value', 'struct nla_bitfield32', '#include<linux/netlink.h>', []],
  ['HAVE_STRUCT_MMSGHDR_MSG_LEN', 'msg_len', 'struct mmsghdr', '#include<sys/socket.h>', ['-D_GNU_SOURCE']],
]

foreach s : check_structs
  if cc.has_member(s.get(2), s.get(1), prefix : s.get(3), args : s.get(4))
    cdata.set(s.get(0), 1)
  endif
endforeach

#enable_uses = [
#  ['__USE_POSIX', 'bits/posix1_lim.h'],
#  ['__USE_XOPEN', 'bits/xopen_lim.h'],
#]
#
#foreach u : enable_uses
#  if cc.has_header(u.get(1))
#    cdata.set(u.get(0), 1)
#  endif
#endforeach

cdata.set('PACKAGE_STRING', '"' + meson.project_name() + ' ' + as_version + '"')
cdata.set('VERSION', '"' + as_version + '"')

if build_machine.system() == 'windows'
	cdata.set('WIN32', 1)
endif

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)

header_files = [
    ['lib', 'string.h'],
    ['lib', 'stdio.h'],
]

conf_headers = configuration_data()
conf_headers.set('INCLUDE_NEXT', 'include_next')
conf_headers.set_quoted('NEXT_STDIO_H', 'stdio.h')
conf_headers.set_quoted('NEXT_STRING_H', 'string.h')

foreach h : header_files
    configure_file(
        input : h.get(0) + '/' + h.get(1) + '.in',
        output : h.get(1),
        configuration : conf_headers,
    )
endforeach


map_files = [
    ['lib', 'sflow.map'],
    ['lib', 'openvswitch.map'],
    ['ovsdb', 'ovsdb.map'],
    ['ofproto', 'ofproto.map'],
    ['vtep', 'vtep.map'],
]

foreach m : map_files
    configure_file(
        input : m.get(0) + '/' + m.get(1) + '.in',
        output : m.get(1),
        configuration : conf_soversion,
    )
endforeach

ovs_lib_version = '0'
ovs_lib_revision = '0'
ovs_lib_age = '0'

conf_version = configuration_data()
conf_version.set('PACKAGE_STRING', meson.project_name() + ' ' + as_version)
conf_version.set('PACKAGE_VERSION', as_version)
conf_version.set('LT_CURRENT', ovs_lib_version)
conf_version.set('LT_REVISION', ovs_lib_revision)
conf_version.set('LT_AGE', ovs_lib_age)

subdir('include')

# MSR: this is temporary hard-coded
# though values are taken from the 'config.log'
# however, most of it should be coming from
# supplied options and have default values
cin_processing = configuration_data()
cin_processing.set('BANNER', '/* -*- mode: c; buffer-read-only: t -*- */') # this a temporary hack and may break backwards compatability with autotools
cin_processing.set('srcdir', meson.project_source_root())
cin_processing.set_quoted('LOGDIR', '/var/log/openvswitch')
cin_processing.set_quoted('RUNDIR', '/var/run/openvswitch')
cin_processing.set_quoted('DBDIR', '/etc/openvswitch')
cin_processing.set_quoted('bindir', '/bin')
cin_processing.set_quoted('sysconfdir', '/etc')
cin_processing.set_quoted('pkgdatadir', '/usr/share/openvswitch')

subdir('python/ovs')

c_in_files = [
    ['lib', 'dirs.c'],
]

foreach cin : c_in_files
    configure_file(
        input : cin.get(0) + '/' + cin.get(1) + '.in',
        output : cin.get(1),
        configuration : cin_processing,
    )
endforeach

global_inc = include_directories(
    '.',
    'include',
    'lib',
)

# MSR: path for pthreads should be collected
# from options and not hardcoded
if build_machine.system() == 'windows'
    global_inc = include_directories(
		'.',
		'include',
		'lib',
		'include/windows',
		'datapath-windows/include',
		'C:/pthreads/pthreads4w',
	)
endif

global_libs = []

add_project_arguments('-Wstrict-prototypes', language : 'c')
add_project_arguments(
    '-Wall',
    '-Wextra',
    '-Wno-sign-compare',
    '-Wpointer-arith',
    '-Wformat',
    '-Wformat-security',
    '-Wswitch-enum',
    '-Wunused-parameter',
    '-Wbad-function-cast',
    '-Wcast-align',
    '-Wstrict-prototypes',
    '-Wold-style-definition',
    '-Wmissing-prototypes',
    '-Wmissing-field-initializers',
    '-Wthread-safety',
    '-fno-strict-aliasing',
    '-Wswitch-bool',
    '-Wlogical-not-parentheses',
    '-Wsizeof-array-argument',
    '-Wshift-negative-value',
#    '-Qunused-arguments',
    '-Wshadow',
    '-Wno-null-pointer-arithmetic',
#    '-Warray-bounds-pointer-arithmetic',
    language : 'c',
)

install_prefix = '/usr/local/'

#ovsidl_files = [
#    ['lib', 'ovsdb-server-idl'],
#    ['lib', 'vswitch-idl'],
#    ['vtep', 'vtep-idl'],
#    ['tests', 'idltest'],
#]

# MSR: file generation probably should be moved to a separate folder with its own meson.build file
lib_ovsdb_server_idl_ovsidl = custom_target(
    'ovsdb-server-idl.ovsidl',
    input : [
        meson.project_source_root() + '/ovsdb/_server.ovsschema',
        meson.project_source_root() + '/lib/ovsdb-server-idl.ann',
    ],
    output : 'ovsdb-server-idl.ovsidl',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'annotate',
        '@INPUT0@',
        '@INPUT1@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

lib_vswitch_idl_ovsidl = custom_target(
    'vswitch-idl.ovsidl',
    input : [
        meson.project_source_root() + '/vswitchd/vswitch.ovsschema',
        meson.project_source_root() + '/lib/vswitch-idl.ann',
    ],
    output : 'vswitch-idl.ovsidl',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'annotate',
        '@INPUT0@',
        '@INPUT1@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

vtep_vtep_idl_ovsidl = custom_target(
    'vtep-idl.ovsidl',
    input : [
        meson.project_source_root() + '/vtep/vtep.ovsschema',
        meson.project_source_root() + '/vtep/vtep-idl.ann',
    ],
    output : 'vtep-idl.ovsidl',
    command : [
        prog_python,
        meson.project_source_root() + '/ovsdb/ovsdb-idlc.in',
        'annotate',
        '@INPUT0@',
        '@INPUT1@',
    ],
    capture : '@OUTPUT@',
    env : python_env,
)

subdir('lib')
subdir('ofproto')
subdir('utilities')
subdir('vtep')
subdir('vswitchd')
subdir('ovsdb')
#subdir('datapath')
