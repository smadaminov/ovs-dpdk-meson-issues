#!/bin/bash

find . -type f -name "*meson.build*" | xargs -I{} cp {} ../ovs-vanilla/{}
find . -type f -name "*\.map\.in" | xargs -I{} cp {} ../ovs-vanilla/{}
cp lib/dirs.c.in ../ovs-vanilla/lib/
cp config.h.meson ../ovs-vanilla/

cp meson_options.txt ../ovs-vanilla/

cp build-aux/extract-odp-netlink-h.py ../ovs-vanilla/build-aux/
cp build-aux/extract-odp-netlink-macros-h.py ../ovs-vanilla/build-aux/
cp build-aux/copy-file-from-build.py ../ovs-vanilla/build-aux/
cp build-aux/extract-odp-netlink-windows-dp-h.py ../ovs-vanilla/build-aux/
