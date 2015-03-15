import nose
from nose.plugins.plugintest import run
import ocgis
from ocgis.test import test_simple
import sys
import os

from cfunits import Units
module_name = os.path.split(test_simple.__file__)[0]

nose.run(argv=[sys.argv[0], module_name, '-v'])