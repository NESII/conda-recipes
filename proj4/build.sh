#!/bin/sh

./configure --prefix=$PREFIX --without-jni

make -j ${CPUCOUNT}
make install
