#!/bin/sh

export DFN="proj-datumgrid-1.5.zip"
wget http://download.osgeo.org/proj/${DFN}
unzip ${DFN} -d ./nad/

./configure --prefix=$PREFIX --without-jni

make -j ${CPUCOUNT}
make install

cp -r ./nad ${PREFIX}
