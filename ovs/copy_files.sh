#!/bin/bash

UPSTREAM_OVS=$1

find . -type f -name "*meson.build*" | xargs -I{} cp {} ${UPSTREAM_OVS}/{}
find . -type f -name "*\.map\.in" | xargs -I{} cp {} ${UPSTREAM_OVS}/{}
cp lib/dirs.c.in ${UPSTREAM_OVS}/lib/
cp config.h.meson ${UPSTREAM_OVS}/

cp meson_options.txt ${UPSTREAM_OVS}/

cp build-aux/extract-odp-netlink-h.py ${UPSTREAM_OVS}/build-aux/
cp build-aux/extract-odp-netlink-macros-h.py ${UPSTREAM_OVS}/build-aux/
cp build-aux/copy-file-from-build.py ${UPSTREAM_OVS}/build-aux/
