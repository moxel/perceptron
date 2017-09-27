import pexpect
import os
import sys

env = os.environ
env.update({'ENV': 'dev'})

child = pexpect.spawn('moxel push -y ci-perceptron:latest', env=env, logfile=sys.stdout.buffer)
try:
    child.expect('Running on http://0.0.0.0:5900/', timeout=360)
    exit(0)
except pexpect.TIMEOUT:
    print('Error: Moxel push timeout')
    exit(1)
