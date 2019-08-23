#!/usr/bin/env python3
"""
download_data_year.py
$ download_data_year.py {-v} -y {year} -r {store_root}
This is a script that downloads a year's worth of race and qualifying data from
the f1 ergast api.
"""
import time
import os
import sys
import argparse

__author__ = "Edie Zhou"
__credits__ = ["Khaled Hemchik: https://github.com/hechmik"]
__license__ = "GPL"
__version__ = "0.0.0"
__maintainer__ = "Edie Zhou"
__email__ = "edie.zhou@utexas.edu"
__status__ = "Development"


def get_inputs():
    """
    Gets inputs for download_data_year,py

    Returns:
        args.years (list): List of years to pull data for
        args.root (str): Root to store json dumps at
    """
    parser = argparse.ArgumentParser(description='Request a year of race and quali data from Ergast API.')
    # parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
    parser.add_argument('-y', dest='years', action='append', help='Year to pull race and qualifying data for')
    parser.add_argument('-r', dest='root', help='Root to store data set at')
    args = parser.parse_args()
    return args.years, args.root

def main():
    years, root = get_inputs()
    print(years)
    print(root)
    return None

if __name__ == "__main__":
    main()
