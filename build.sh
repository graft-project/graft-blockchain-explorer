#!/bin/sh

mkdir build
cd build
cmake -DMONERO_DIR=<path-to>/graft-project/GraftNetwork/ ..

make -j8
