import mmap
import re
import sys

hfile=sys.argv[1]

# 'line_start' is the line number where the definition of the struct begin
# 'line_end' is the line number where the definition of the struct ends
def generate_fields_macros(struct_name):
    with open(hfile, 'r') as f:
        define_lines = []
        found = False
        for line in f:
            if found:
                tmp_line = re.sub(";.*", "", line)
                fields = re.split("\s+", tmp_line)
                if len(fields) == 5:
                    define_lines.append("    {offsetof(struct " + struct_name + ", " + fields[3] + "), sizeof(" + fields[1] + " " + fields[2] + ")}, \\")
                elif len(fields) == 4:
                    define_lines.append("    {offsetof(struct " + struct_name + ", " + fields[2] + "), sizeof(" + fields[1] + ")}, \\")
                else:
                    define_lines.append("    {0, 0}}")
                    break
            elif re.search(r'\b' + struct_name + r'\b', line):
                if "{" in line:
                    found = True
        STRUCT = struct_name.upper()
        define_line = "#define " + STRUCT + "_OFFSETOF_SIZEOF_ARR { \\"
        print(define_line)
        for define_line in define_lines:
            print(define_line)
        print()
        print()

preamble = ("""/* Generated automatically from <include/odp-netlink.h> -- do not modify! */
#ifndef ODP_NETLINK_MACROS_H
#define ODP_NETLINK_MACROS_H

""")

print(preamble)

generate_fields_macros("ovs_key_ethernet")
generate_fields_macros("ovs_key_ipv4")
generate_fields_macros("ovs_key_ipv6")
generate_fields_macros("ovs_key_tcp")
generate_fields_macros("ovs_key_udp")
generate_fields_macros("ovs_key_sctp")
generate_fields_macros("ovs_key_icmp")
generate_fields_macros("ovs_key_icmpv6")
generate_fields_macros("ovs_key_arp")
generate_fields_macros("ovs_key_nd")
generate_fields_macros("ovs_key_nd_extensions")

epilogue = ("""
#endif""")

print(epilogue)
