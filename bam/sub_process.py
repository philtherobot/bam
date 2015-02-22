
import subprocess as _subprocess

def call(cmd):
    print('running "{}"'.format(cmd))
    _subprocess.call(cmd, shell=True)
