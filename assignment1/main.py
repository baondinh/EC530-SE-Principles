#!/usr/bin/env python3

"""
Main executable 
Related functions stored in geo_functions.py

CSV taken from Boston 311 Service Request Historical Data
https://data.boston.gov/dataset/311-service-requests
TODO: Provided CSVs store latitude/longitude as floats, but need to introduce datatype checking and valid CSV formatting
"""

import sys 
import logging
from geo_functions import *
from accessory_functions import *

def main(): 
    # Setup 
    try: 
        script_folder = get_script_folder()
        output_folder = script_folder / "output"
        csv_file = script_folder / "data" / "tmpx_n76cvi.csv"
        logger = create_logger(script_folder)
    except: 
        raise

    # 1) Get two sets of latitude/longitude coordinates 
    try: 
        df = get_geo_coordinates(csv_file)
        print(df)
        logger.info(f"Successfully obtained geo coordinates")
    except Exception as e: 
        logger.error(f"Unable to obtain geo coordinates from CSV - {e}")

    # 2) Get random points of data 
    try: 
        # Randomly sample rows of data
        sampled1 = df.sample(n=10, random_state=None)
        sampled2 = df.sample(n=10, random_state=None)

        # Extract points as tuples
        points1: list[Point] = list(
            zip(sampled1["latitude"], sampled1["longitude"])
        )
        points2: list[Point] = list(
            zip(sampled2["latitude"], sampled2["longitude"])
        )

        # p1, p2 = points
        # print("Point 1:", p1)
        # print("Point 2:", p2)

        print(points1)
        print(points2)
        logger.info("Successfully sampled random points of data")
    except Exception as e: 
        logger.error(f"Unable to create random arrays of geo coordinates - {e}")

    # 3) For each point in first array, find closest point in second array using Haversine distance
    try: 
        print("potato")
    except Exception as e: 
        logger.error(f"asd;flkasjd;flkajs;dflkj")

if __name__ == "__main__": 
    main()