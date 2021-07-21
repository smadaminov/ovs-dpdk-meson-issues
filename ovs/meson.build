# SPDX-License-Identifier: BSD-3-Clause
# Copyright(c) 2021 VMware, Inc.

project('openvswitch', 'C',
        version: '2.16.90',
        license: 'Apache2.0',
        default_options: ['buildtype=release', 'default_library=static'],
        meson_version: '>= 0.49.2'
)

as_version = meson.project_version()
ver_arr = as_version.split('.')

as_current_version  = ver_arr[0]
as_revision_version = ver_arr[1]
as_age_version      = ver_arr[2]

cc = meson.get_compiler('c')

cdata = configuration_data()
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
  ['HAVE_CLOCK_GETTIME', 'clock_gettime', '#include<time.h>'],
# check token ['HAVE_CXX11']
# check token ['HAVE_DECL_MALLOC_TRIM']
# check token ['HAVE_DECL_RTE_EAL_NUMA_AWARE_HUGEPAGES']
# check token ['HAVE_DECL_RTE_LIBRTE_VHOST_NUMA']
# check token ['HAVE_DECL_STRERROR_R']
# check token ['HAVE_DECL_SYS_SIGLIST']
# check token ['HAVE_GCC4_ATOMICS']
  ['HAVE_GETLOADAVG', 'getloadavg', '#include<stdlib.h>'],
  ['HAVE_GETMNTENT_R', 'getmntent_r', '#include<mntent.h>'],
# check token ['HAVE_GLIBC_PTHREAD_SETNAME_NP']
# check token ['HAVE_IF_DL']
# check token ['HAVE_LIBCAPNG']
# check token ['HAVE_LIBSOCKET']
# check token ['HAVE_MLOCKALL']
# check token ['HAVE_NETBSD_PTHREAD_SETNAME_NP']
# check token ['HAVE_NETLINK']
# check token ['HAVE_NLA_BITFIELD32']
# check token ['HAVE_OPENSSL']
  ['HAVE_POSIX_MEMALIGN', 'posix_memalign', '#include<stdlib.h>'],
# check token ['HAVE_PRAGMA_MESSAGE']
  ['HAVE_PTHREAD_SET_NAME_NP', 'pthread_set_name_np', '#include<pthread.h>'],
# check token ['HAVE_PTHREAD_SPIN_LOCK']
# check token ['HAVE_SCTP_CONNTRACK_HEARTBEATS']
  ['HAVE_SENDMMSG', 'sendmmsg', '#include<sys/socket.h>'],
  ['HAVE_STATVFS', 'statvfs', '#include<sys/statvfs.h>'],
  ['HAVE_STRERROR_R', 'strerror_r', '#include<string.h>'],
# check token ['HAVE_STRNLEN']
# check token ['HAVE_STRTOK_R_BUG']
# check token ['HAVE_STRUCT_IFREQ_IFR_FLAGSHIGH']
# check token ['HAVE_STRUCT_MMSGHDR_MSG_LEN']
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

check_structs = [
  ['HAVE_NLA_BITFIELD32', 'value', 'struct nla_bitfield32'],
]

foreach f : check_functions
  if cc.has_function(f.get(1), prefix : f.get(2))
    cdata.set(f.get(0), 1)
  endif
endforeach

foreach s : check_structs
  if cc.has_member(s.get(2), s.get(1), prefix : '#include<linux/netlink.h>')
    cdata.set(s.get(0), 1)
  endif
endforeach

cdata.set('PACKAGE_STRING', '"' + meson.project_name() + ' ' + as_version + '"')
cdata.set('VERSION', '"' + as_version + '"')

configure_file(input : 'config.h.meson',
  output : 'config.h',
  configuration : cdata)

global_inc = include_directories(
    '.',
    'include',
    'lib',
)

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
#    '-Wthread-safety',
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

subdir('lib')
#subdir('datapath')
