#! /usr/bin/env python
import os
import subprocess

home = os.environ['HOME']
bashrc = os.path.join(home, '.bashrc')
deployment_path = os.path.dirname(os.path.realpath(__file__)).lstrip(home)
source_file_path = '$HOME/%s/scripts/source.sh' % deployment_path
source_line = 'source %s' % source_file_path

found = False
for line in open(bashrc):
    if source_line in line:
        found = True

if not found:
    lines = []
    lines.append('\nif [ -f %s ]; then\n' % source_file_path)
    lines.append('\t' + source_line + '\n')
    lines.append('fi')
    open(bashrc, 'a').writelines(lines)
    subprocess.call('. ~/.bashrc', shell=True)
