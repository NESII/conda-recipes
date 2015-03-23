from ocgis.test import run
import os
import subprocess
print(subprocess.check_call(['which', 'python']))
tdk

test_target = os.environ.get('CBUILD_OCGIS_TEST_TARGET')
if test_target == 'simple' or test_target is None:
    simple = True
elif test_target == 'all':
    simple = False
else:
    raise NotImplementedError(test_target)

run(simple=simple)