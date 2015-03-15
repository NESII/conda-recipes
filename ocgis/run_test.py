import nose
from nose.plugins.plugintest import run
import ocgis
from ocgis.test import test_simple
import sys


module_name =test_simple.__file__
print module_name

nose.run(argv=[sys.argv[0], module_name, '-v'])