# This program parses the original parquet files into the desired format for this project, i.e., filtering by American Airlines only as well as merging all the data into a single parquet file.
# Coded by Jofre Faraudo for a coursework on behalf of all the team. 2026

# Imports
import pandas as pd

# OPTIONS - Play with these to change program behaviour
FILTER_BY_AIRLINE = "AAL" # Callsign (startswith). Change to empty string "" to disable filtering.
SKIP_DATA = ["ukwaypoints", "globalwaypoints"] # Datasets to be omitted when parsing

# SETTINGS - General configuration parameters
# Files to read
FILES = {"metadata":"./data_raw/metadata-global/2021-07-0{}-metadata.pq", "ukwaypoints":"./data_raw/wypts-uk-hi-res/spire-uk-2021070{}.pq", "globalwaypoints":"./data_raw/wypts-global/2021-07-0{}-waypoints.pq"} # Format: dataset name -> raw data path. Restricted access to files.
OUTPUT = "./data_parsed/{}.pq"
first = 1
last = 7

# ACTUAL CODE
# Looping over all datasets
for n, p in FILES.items():
    # Skip?
    if n in SKIP_DATA:
        continue

    # Unpack
    i = first
    frames = []
    while i <= last:
        # Read data from parquet
        frames.append(pd.read_parquet(p.format(i)))

        # Filter - Done using an if structure rather than filter argument to simplify code and understanding
        if type(FILTER_BY_AIRLINE) == str and FILTER_BY_AIRLINE != "":
            frames[-1] = frames[-1][frames[-1]["callsign"].str.match(FILTER_BY_AIRLINE)] # str.match ensures partial match at the beginning of the string only (startwith operator)

        # Add day index to know where each row comes from
        frames[-1].insert(0,"Date",i)
        i += 1
    merge = pd.concat(frames) # Using a list to avoid unecessary copies

    # Saving
    merge.to_parquet(OUTPUT.format(n))
    #print(merge)
