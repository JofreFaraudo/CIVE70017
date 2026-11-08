import pandas as pd

# Files
LOAD = "./data_parsed/metadata.pq"
SAVE = "./data_parsed/AAmainline.pq"

# Models to exclude or include
LIST = ['E75L', 'E145', 'CRJ7']
IS_WHITELIST = False # True: only models in list will be saved - whitelist mode. False: models in list will be dropped - blacklist mode.


# Actual code

df = pd.read_parquet(LOAD, filters=[("aircraft_type_icao", "in" if IS_WHITELIST else "not in", )])
print(df["aircraft_type_icao"].unique())
#df.to_parquet(SAVE)
