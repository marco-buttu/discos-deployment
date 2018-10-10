#!/usr/bin/env python
from __future__ import print_function
import sys
import os
import subprocess

def queryYesNo(question):
    valid = {
        '': True,
        'yes': True,
        'y': True,
        'ye': True,
        'no': False,
        'n': False
    }

    for _ in range(3):
        sys.stdout.write(question + ' [Y/n]: ')
        choice = raw_input().lower()
        try:
            return valid[choice]
        except KeyError:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').")

    print("ERROR: please, respond with 'yes' or 'no' (or 'y' or 'n').")
    sys.exit(2)

if sys.version_info[0] != 2 or sys.version_info[1] != 7:
    print('ERROR: the setup procedure and the scripts require Python 2.7!')
    sys.exit(1)

if queryYesNo('Would you like to automatically install the requirements?'):
    requirements = [
        'pexpect'
    ]
    FNULL = open(os.devnull, 'w')
    for requirement in requirements:
        sys.stdout.write("Installing '{}' package...".format(requirement))
        sys.stdout.flush()
        subprocess.call(
            ['pip', 'install', requirement],
            stdout=FNULL,
            stderr=FNULL
        )
        print('done.')

if not queryYesNo('Would you like to add the scripts to your ~/.bashrc file?'):
    sys.exit(0)

home = os.environ['HOME']
bashrc = os.path.join(home, '.bashrc')
deployment_path = os.path.dirname(os.path.realpath(__file__)).lstrip(home)
source_file_path = '$HOME/{}/scripts/source.sh'.format(deployment_path)
source_line = 'source {}'.format(source_file_path)

found = False
for line in open(bashrc):
    if source_line in line:
        found = True

if found:
    print('The scripts are already installed. Nothing to do.')
    sys.exit(0)
else:
    lines = []
    lines.append('\nif [ -f {} ]; then\n'.format(source_file_path))
    lines.append('    ' + source_line + '\n')
    lines.append('fi')
    open(bashrc, 'a').writelines(lines)
    print(
        'The file that sources the scripts has been '
        + 'added to your ~/.bashrc file. They will '
        + 'be available as soon as you open a new '
        + 'terminal. Have fun!'
    )
    sys.exit(0)
