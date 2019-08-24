import os
from setuptools import setup

def read(fname):
    """
    Purpose: 
        Utility function to read in file from same directory

    Args:
        fname (str): File name

    Returns:
        file_contents (str): Contents of the file 
    """
    file_path = os.path.join(os.path.direname(__file__), fname)
    file_contents = open(file_path).read()
    return file_contents

setup(
    name = 'f1_stats'

    # Package metadata
    version = '0.0.1',
    author = 'Edie Zhou',
    author_email = 'edie.zhou@utexas.edu',
    description = 'Python package for f1 stats and visualizations',
    long_description = read('README'),
    license = 'MIT'
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

)
