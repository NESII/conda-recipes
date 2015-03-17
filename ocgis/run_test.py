import nose
from nose.plugins.plugintest import run
import ocgis
from ocgis import test
import sys
import os

from cfunits import Units
module_name = os.path.split(test.__file__)[0]
from ocgis.test.test_misc import test_dependency_versions
#tdk: make this work for simple and all tests
# module_name = test_dependency_versions.__file__
os.environ['OCGIS_DIR_SHPCABINET'] = os.path.expanduser('~/data/ocgis_test_data/shp')
os.environ['OCGIS_DIR_TEST_DATA'] = os.path.expanduser('~/data/ocgis_test_data/nc')
from ocgis import env
print(env.DIR_TEST_DATA)
sys.exit(1)
result = nose.run(argv=[sys.argv[0], module_name, '-v', '-a', '!slow,!remote,!esmpy7'])
if not result:
    sys.exit(1)