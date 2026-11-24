import pandas as pd
from os import listdir as ls

DIR = "./data_parsed/"
FLIGHTS = "./data_parsed/flights.pq"
SAVE = "./data_parsed/ccd.pq"
CSV = "./data_parsed/ccd.csv"

emissions = pd.concat([pd.read_parquet(DIR+f) for f in ls(DIR) if f.startswith("cruise") and f.endswith(".pq")])
emissions.reset_index(inplace=True, drop=True)

flights = pd.read_parquet(FLIGHTS)
df = pd.concat([flights, emissions], axis=1)

print(df)
df.to_parquet(SAVE)
df.to_csv(CSV)