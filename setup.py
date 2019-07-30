# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__ *= *\'(.*)\'',
    open('distro/distro.py').read(),
    re.M
).group(1)

with open('README.md', 'rb') as f:
    long_descr = f.read().decode('utf-8')

setup(
    name='distro-names',
    packages=['distro'],
    entry_points={
        'console_scripts': ['distro = distro.distro:main']
    },
    version=version,
    description='Search for OS Names and Versions',
    long_description=long_descr,
    long_description_content_type='text/markdown',
    author='Igor Gentil',
    author_email='igor@devops.cool',
    url='https://github.com/igorlg/distro-names/',
)
