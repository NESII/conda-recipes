from ocgis.test import run
import os


test_target = os.environ.get('CBUILD_OCGIS_TEST_TARGET')
if test_target == 'simple' or test_target is None:
    attrs = 'simple'
elif test_target == 'all':
    simple = '!slow,!remote,!esmpy7'
else:
    raise NotImplementedError(test_target)

run(attrs=attrs)