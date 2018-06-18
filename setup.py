#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: skip-file

from setuptools import setup
from setuptools import find_packages

import re
import os
import sys
from pkg_resources import parse_version

# load version form _version.py
exec(open("maily/_version.py").read())

# Dependencies of GPflow
requirements = []

packages = find_packages('.')
package_data={'maily': ['maily/borc']}

setup(name='maily',
      version=__version__,
      author="Justin Beland",
      author_email="jbeland151@gmail.com",
      description=("automated e mail notification"),
      license="None",
      keywords="mail automated fun useful",
      #url="http://github.com/GPflow/GPflow",
      packages=packages,
      install_requires=requirements,
      tests_require=['pytest'],
      package_data=package_data,
      include_package_data=True,
      test_suite='tests',
      classifiers=[
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ])
