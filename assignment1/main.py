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
    except Exception as e: 
        logger.error(f"Unable to obtain geo coordinates from CSV - {e}")


if __name__ == "__main__": 
    main()