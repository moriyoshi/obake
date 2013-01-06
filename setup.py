#!/usr/bin/env python

import os
import sys
from setuptools import setup
from setuptools import find_packages
from types import *

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'zope.interface',
    'pyobjc-core >= 2.3.2a0',
    'pyobjc-framework-WebKit >= 2.3.2a0',
    ]

test_requires = [
    'py-dom-xpath',
    ]

setup(
    name='obake',
    version="0.0.1",
    description='OMG IDL parser and code generator',
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Environment :: MacOS X :: Cocoa",
        "Environment :: X11 Applications :: GTK",
        "Environment :: Win32 (MS Windows)",
        ],
    author='obake',
    author_email='mozo@mozo.jp',
    url='http://github.com/moriyoshi/obake',
    package_dir={'':'src'},
    packages=find_packages('src'),
    include_package_data=True,
    setup_requires=requires,
    install_requires=requires,
    tests_require=requires,
    test_suite='obake.tests'
    )
