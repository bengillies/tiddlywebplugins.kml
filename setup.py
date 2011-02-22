# YOU NEED TO EDIT THESE
AUTHOR = 'Ben Gillies'
AUTHOR_EMAIL = 'bengillies@gmail.com'
NAME = 'tiddlywebplugins.kml'
DESCRIPTION = 'Adds support for KML files'
VERSION = '0.1'


import os

from setuptools import setup, find_packages


# You should carefully review the below (install_requires especially).
setup(
    namespace_packages = ['tiddlywebplugins'],
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = AUTHOR,
    url = 'http://pypi.python.org/pypi/%s' % NAME,
    packages = find_packages(exclude='test'),
    author_email = AUTHOR_EMAIL,
    platforms = 'Posix; MacOS X; Windows',
    install_requires = ['setuptools', 'tiddlyweb>=1.2.0', 'pykml>=0.0.3'],
    zip_safe = False
    )
