# This is a "python" script that transforms <linux/openvswitch.h> into a
# form that is suitable for inclusion within the Open vSwitch tree on
# Windows system. The transformed header file can be included by Windows
# driver modules.

import re
import sys

# Add a header warning that this is a generated file.
banner = ("""/* -*- mode: c; buffer-read-only: t -*- */
/* Generated automatically from <linux/openvswitch.h> -- do not modify! */



""")

header_template = sys.argv[1]
with open(header_template, 'r') as f:
    contents = f.readlines()

contents.insert(0, banner)
contents = "".join(contents)

# Avoid using reserved names in header guards.
contents = re.sub("_LINUX_OPENVSWITCH_H", "__OVS_DP_INTERFACE_H", contents)

# and use the appropriate userspace header.
contents = re.sub("<linux/types.h>", "Types.h", contents)

# Add ETH_ADDR_LEN macro to avoid including userspace packet.h
eth_addr_len_macro = ("""
#ifndef ETH_ADDR_LEN
#define ETH_ADDR_LEN 6
#endif
""")
contents = re.sub("#include <linux/if_ether.h>", eth_addr_len_macro, contents)

# Use OVS's own ETH_ADDR_LEN instead of Linux-specific ETH_ALEN.
contents = re.sub("ETH_ALEN", "ETH_ADDR_LEN", contents)

print(contents)
