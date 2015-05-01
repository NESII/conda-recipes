#!/bin/bash

export CFLAGS="-I${PREFIX}/include $CFLAGS"
export LDFLAGS="-L${PREFIX}/lib $LDFLAGS"

${PYTHON} setup.py install || exit 1;
