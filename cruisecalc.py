#import xlwings as wg
import pandas as pd
from time import sleep

# Files
LOAD = "./data_parsed/metadata.pq"
WORKBOOK = r".\main.xlsm"
SHEET = "Emissions calculator"
SAVE = "./data_parsed/cruise.pq"

# General parameters
MODEL = "C11"
CCD = "D21"
RESULTS = "G21:P21"
HEADERS = "G17:P17"
MODELS = ["A319", "B77W", "B772", "B738", "B38M", "A320", "A21N", "A321", "B789", "B788"]
NM_TO_KM = 1.852

"""
# Excel setup
app = wg.App(visible=False, add_book=False)
app.screen_updating = False

sheet.range(MODEL).value = "A319"
sheet.range(CCD).value = 
print(sheet.range(RESULTS).value)

"""
# Load files
flights = pd.read_parquet(LOAD, filters=[[("aircraft_type_icao", "==", model)] for model in MODELS])
print(flights)
maxs = flights.groupby("aircraft_type_icao", as_index=False)["total_distance_km"].max()
print(maxs)
maxs["dist_nm"] = maxs["total_distance_km"]/NM_TO_KM
print(maxs)
maxs.to_csv("./data_parsed/ranges.csv")


"""
wb = app.books.open(WORKBOOK)
sheet = wb.sheets[SHEET]

emdata = []

for case in df.itertuples():
    sheet.range(MODEL).value = case.aircraft_type_icao
    # stage
    sleep(0)
    emdata.append(sheet.range(RESULTS).value)
    sleep(0)


# Saving new data into dataframe
results = pd.concat([df, pd.DataFrame(emdata, columns=sheet.range(HEADERS).value)], axis=1)
print(results)
#print(emdata)
results.to_parquet(SAVE)
"""

"""
# Closing excel file
wb.close()
app.quit()
"""
