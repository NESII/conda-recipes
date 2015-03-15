import os
import subprocess


curr = os.getcwd()
try:
    os.chdir(os.environ['SRC_DIR'])
    subprocess.check_call([os.environ['PYTHON'], 'setup.py', 'test'])
finally:
    os.chdir(curr)