#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def walk_subpkg(name):
    data_files = []
    package_dir = 'pathways'
    for parent, _, files in os.walk(os.path.join(package_dir, name)):
        # Remove package_dir from the path.
        sub_dir = os.sep.join(parent.split(os.sep)[1:])
        for _file in files:
            data_files.append(os.path.join(sub_dir, _file))
    return data_files


def get_version():
    _version = {}
    with open('pathways/_version.py') as fp:
        exec(fp.read(), _version)
    return _version['__version__']


REQUIRES = [
    'appdirs>=1.4.3,<2.0',
    'jinja2>=2.10.1,<3.0',
    'pandas>=0.25.0',
    'geopandas>=0.6.0,<1.0',
    'unidecode>=1.1.0,<2.0',
    'semantic_version>=2.8.0,<3',
    'requests>=2.25.1',
    'aiohttp>=3.6.1',
    'tqdm>=4.61.2'
]


EXTRAS_REQUIRES_TESTS = [
    'pytest',
    'pytest-mock',
    'pylint',
    'flake8'
]


PACKAGE_DATA = {
    '': [
        'LICENSE',
        'CONTRIBUTORS',
    ],
    'pathways': [
        'assets/*',
        'assets/*.j2'
    ] + walk_subpkg('assets'),
}


DISTNAME = 'pathways'
DESCRIPTION = 'pathways Python package for data scientists'
LICENSE = 'BSD'
URL = 'https://github.com/geraldinejones/p4p-monorepo'
AUTHOR = 'Yogesh Dhanapal'
EMAIL = 'geoyogesh@gmail.com'


setup(
    name=DISTNAME,
    version=get_version(),

    description=DESCRIPTION,
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    license=LICENSE,
    url=URL,

    author=AUTHOR,
    author_email=EMAIL,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    keywords=['pathways', 'data', 'science', 'maps', 'spatial', 'pandas', 'geopandas', 'transportation', 'planning'],

    packages=find_packages(),
    package_data=PACKAGE_DATA,
    package_dir={'pathways': 'pathways'},
    include_package_data=True,

    install_requires=REQUIRES,
    extras_require={
        'tests': EXTRAS_REQUIRES_TESTS
    },
    python_requires='>=3.5'
)
