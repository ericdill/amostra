__author__ = 'arkilic'
try:
    from setuptools import setup
except ImportError:
    try:
        from setuptools.core import setup
    except ImportError:
        from distutils.core import setup

import versioneer
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='amostra',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="BSD (3-clause)",
    url="https://github.com/NSLS-II/amostra.git",
    packages=['amostra',
              'amostra.client'
              ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        'Programming Language :: Python :: 3',
    ],
)
