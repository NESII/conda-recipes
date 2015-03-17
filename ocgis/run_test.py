import nose
from nose.plugins.plugintest import run
import ocgis
from ocgis import test
import sys
import os
from ocgis.test.test_real_data import test_narccap

from cfunits import Units
module_name = os.path.split(test_narccap.__file__)[0]+':TestRotatedPole'
from ocgis.test.test_misc import test_dependency_versions
#tdk: make this work for simple and all tests
# module_name = test_dependency_versions.__file__
os.environ['OCGIS_DIR_SHPCABINET'] = os.path.expanduser('~/data/ocgis_test_data/shp')
os.environ['OCGIS_DIR_TEST_DATA'] = os.path.expanduser('~/data/ocgis_test_data')
result = nose.run(argv=[sys.argv[0], module_name, '-vx', '-a', '!slow,!remote,!esmpy7'])
if not result:
    sys.exit(1)