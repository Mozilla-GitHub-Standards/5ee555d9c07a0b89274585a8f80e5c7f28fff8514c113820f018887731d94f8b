#! /usr/bin/env python

from pip.req import parse_requirements
from setuptools import setup, find_packages
import os
import sys

deps = [
    'pefile==2016.3.28',
    'requests',
    'six',
]

setup(
    name="signtool",
    version="2.0.0a",
    description="Mozilla Signing Tool",
    author="Release Engineers",
    author_email="release+python@mozilla.com",
    packages=find_packages(exclude="tests"),
    test_suite='tests',
    zip_safe=False,
    license="MPL 2.0",
    install_requires=deps,
    entry_points={
        'console_scripts': [
            'signtool = signtool.signtool:main'
        ],
    },
    # include files listed in MANIFEST.in
    include_package_data=True,
    classifiers=(
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ),
)