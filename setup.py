import os
from setuptools import setup
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


setup(
    name = 'f1_stats',

    # Package metadata
    version = '0.0.1',
    author = 'Edie Zhou',
    author_email = 'edie.zhou@utexas.edu',
    description = 'Python package for f1 stats and visualizations',
    license = 'MIT',
    url = 'https://github.com/edie-zhou/f1_stats',

    # Package structure

    # Package dependencies, never trust IDE to find packages
    install_requires = ['numpy',
                        'matplotlib',
                        'pandas',
                        'requests',
                        'setuptools',],
    classifiers = [
        'Programming Langauge :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    distclass=BinaryDistribution,

)
