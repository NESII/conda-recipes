#!/bin/bash
exit 1
export GDAL_DATA="${PREFIX}/share/gdal"

${PYTHON} setup.py install || exit 1;
