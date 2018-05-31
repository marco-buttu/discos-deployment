import os
import sys
import tempfile
from jinja2 import Template

template = Template(open('templates/discos-deploy').read())
script = open('scripts/discos-deploy', 'w')
script.write(template.render(root_dir=os.path.dirname(os.path.realpath(__file__))))
script.close()

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='discos-deployment',
    version='0.1',
    scripts=[
        'scripts/discos-deploy',
        'scripts/discos-vms',
        'scripts/discos-login'
    ],
    license='GPL',
    platforms='all',
)
os.remove('scripts/discos-deploy')
