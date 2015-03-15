import os
import subprocess


subprocess.check_call(['cd', os.environ['SRC_DIR'], '&&', os.environ['PYTHON'], 'setup.py', 'test'])