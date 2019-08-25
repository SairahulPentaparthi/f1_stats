#!/usr/bin/env python3
"""
download_data_year.py
$ download_data_year.py {-v} -y {year} -n {num_rounds} -r {store_root}
e.g.:$ download_data_year.py -y 2018 -n 21 -r /home/user/dataset

This is a script that downloads a year's worth of race and qualifying data from
the f1 ergast api.
"""

import argparse
import datetime as dt
import json
import os
import sys
import time

import requests

__author__     = "Edie Zhou"
__credits__    = ["Khaled Hemchik: https://github.com/hechmik"]
__license__    = "MIT"
__version__    = "0.0.1"
__maintainer__ = "Edie Zhou"
__email__      = "edie.zhou@utexas.edu"
__status__     = "Development"


def get_inputs():
    # TODO: Find a way to detect number of rounds in a year, use google to find number of races in a year for now
    """
    Purpose:
        Gets inputs for download_data_year,py

    Returns:
        args.years     (list): List of year strings to pull data for
        args.root       (str): Root to store json dumps at
        args.num_rounds (str): Number of rounds in yeaer
    """
    parser = argparse.ArgumentParser(description='Request a year of race and qualifying data from Ergast API.')
    # parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
    parser.add_argument('-y', dest='years', action='append', help='Year to pull race and qualifying data for')
    parser.add_argument('-r', dest='root', help='Root to store data set at')
    parser.add_argument('-n', dest='num_rounds', help='Number of rounds in year')
    args = parser.parse_args()
    return args.years, args.root, args.num_rounds


def request_data(base_url, num_rounds, session, year='2018', dataset_root='/home/ezhou/Documents/dataset/'):
    """
    Purpose:
        Requests data from the online Ergast formula 1 api and dumps it into a user specified directory

    Params:
        base_url        (string): API URL
        number_of_rounds   (int): Number of rounds in a season
        session_name    (string): Type of session e.g.:'race', 'qualy'
        season          (string): Season to pull data from
        dataset_root    (string): Root to store dataset in

    Returns:
        None
    """
    for round in range(1, num_rounds + 1):
        current_round_data_url = base_url.format(round=round)
        current_round_data = requests.get(current_round_data_url).json()
        filename = "{}{}_{}_{}.json".format(dataset_root, int(year), round, session)
        print(filename)
        with open(filename, 'w') as f:
            json.dump(current_round_data, f)

        # Minimize load on API servers
        time.sleep(5)

    return None


def download_quali_and_race_data(years, root, num_rounds=21):
    """
    Purpose:
        Downloads qualifying and race data from a round and saves it into a base root dir

    Params:
        years     (list): List of year strings to pull data for
        root       (str): User input root dir of dataset
        num_rounds (str): Number of rounds in year

    Returns:
        None
    """
    for year in years:
        api_url = "http://ergast.com/api/f1/{year}/{round}/{session}.json"
        qualy_url = api_url.format(year=year, session='qualifying')
        race_url = api_url.format(year=year, session='race')
        print("Download qualifying data for {year}".format(year=year))
        request_data(base_url=qualy_url, num_rounds=num_rounds, session="qualy",
                     year=year, dataset_root=root)
        print("Download race data for {year}".format(year=year))
        request_data(base_url=race_url, num_rounds=num_rounds, session="race",
                     year=year, dataset_root=root)

    return None


def main():
    years, root, num_rounds= get_inputs()
    print(years)
    download_quali_and_race_data(years, root, num_rounds)

    return None


if __name__ == "__main__":
    main()
