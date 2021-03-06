# This is a "python" script that transforms <linux/openvswitch.h> into a
# form that is suitable for inclusion within the Open vSwitch tree on
# both Linux and non-Linux systems including Windows.

import re
import sys

banner = ("""/* -*- mode: c; buffer-read-only: t -*- */
/* Generated automatically from <linux/openvswitch.h> -- do not modify! */



""")

win_defs = ('''
#ifdef _WIN32
#include "OvsDpInterfaceExt.h"
#include "OvsDpInterfaceCtExt.h"
#endif

/* IPCT_* enums may not be defined in all platforms, so do not use them. */
#define OVS_CT_EVENT_NEW	(1 << 0)   /* 1 << IPCT_NEW */
#define OVS_CT_EVENT_RELATED	(1 << 1)   /* 1 << IPCT_RELATED */
#define OVS_CT_EVENT_DESTROY	(1 << 2)   /* 1 << IPCT_DESTROY */
#define OVS_CT_EVENT_REPLY	(1 << 3)   /* 1 << IPCT_REPLY */
#define OVS_CT_EVENT_ASSURED	(1 << 4)   /* 1 << IPCT_ASSURED */
#define OVS_CT_EVENT_PROTOINFO	(1 << 5)   /* 1 << IPCT_PROTOINFO */
#define OVS_CT_EVENT_HELPER	(1 << 6)   /* 1 << IPCT_HELPER */
#define OVS_CT_EVENT_MARK	(1 << 7)   /* 1 << IPCT_MARK */
#define OVS_CT_EVENT_SEQADJ	(1 << 8)   /* 1 << IPCT_SEQADJ */
#define OVS_CT_EVENT_SECMARK	(1 << 9)   /* 1 << IPCT_SECMARK */
#define OVS_CT_EVENT_LABEL	(1 << 10)  /* 1 << IPCT_LABEL */

#define OVS_CT_EVENTMASK_DEFAULT \\
  (OVS_CT_EVENT_NEW | OVS_CT_EVENT_RELATED | OVS_CT_EVENT_DESTROY |\\
   OVS_CT_EVENT_MARK | OVS_CT_EVENT_LABEL)


''')

header_template = sys.argv[1]
with open(header_template, 'r') as f:
    contents = f.readlines()

# Add a header warning that this is a generated file.  It might save somebody
# some frustration (maybe even me!).
contents.insert(0, banner)

# Include platform extensions header file on Win32.
contents.insert(len(contents) - 1, win_defs)

contents = "".join(contents)

# Avoid using reserved names in header guards.
contents = re.sub("_LINUX_OPENVSWITCH_H", "ODP_NETLINK_H", contents)

# Use OVS's own struct eth_addr instead of a 6-byte char array.
contents = re.sub("<linux/types.h>", "\"openvswitch/types.h\"", contents)
contents = re.sub("<linux/if_ether.h>", "<netinet/in.h>", contents)
contents = re.sub("__u8\s+([a-zA-Z0-9_]*)\s*\[\s*ETH_ALEN\s*\]", "struct eth_addr \\1", contents)

# Transform IPv6 addresses from an array to struct in6_addr
#
# As a very special case, only transform member names with more than
# one character because struct ovs_key_nsh has a member "__be32 c[4];"
# that is not an IPv6 address.
contents = re.sub("__be32\s+([a-zA-Z0-9_]{2,})\s*\[\s*4\s*\]", "struct in6_addr \\1", contents)

# Transform most Linux-specific __u<N> types into C99 uint<N>_t types,
# and most Linux-specific __be<N> into Open vSwitch ovs_be<N>,
# and use the appropriate userspace header.
contents = re.sub("__u32", "uint32_t", contents)
contents = re.sub("__u16", "uint16_t", contents)
contents = re.sub("__u8", "uint8_t", contents)
contents = re.sub("__be32", "ovs_be32", contents)
contents = re.sub("__be16", "ovs_be16", contents)

# Transform 64-bit Linux-specific types into Open vSwitch specialized
# types for 64-bit numbers that might only be aligned on a 32-bit
# boundary.
contents = re.sub("__u64", "ovs_32aligned_u64", contents)
contents = re.sub("__be64", "ovs_32aligned_be64", contents)

print(contents)
