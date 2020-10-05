#!/usr/bin/env python

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'VERSION')) as version_file:
    VERSION = version_file.read().strip()


setup(
    name='fcurellatestproject',
    version=VERSION,
    description="",
    long_description="",
    author='fcurella',
    author_email='flavio.curella@gmail.com',
    url='https://github.com/fcurella/testrepo',
    license='MIT License',
    packages=find_packages(exclude=[]),
    platforms=["any"],
    zip_safe=True,
    python_requires=">=3.5",
)
