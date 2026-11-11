import xlwings as wg
import pandas as pd
from time import sleep

# Files
DATASET = "./data_parsed/operations.pq"
WORKBOOK = r".\lto3.xlsm"
SHEET = "LTO emissions calculator"
SAVE = "./data_parsed/LTO.pq"

# Sheets parameters
MODEL = "F14"
AIRPORT = "F24"
TAKEOFF = "V40:V48"
LANDING = "AK40:AK48"
HEADERS = "C40:C48"

# Excel setup
app = wg.App(visible=False, add_book=False)
app.screen_updating = False

# Opening files
df = pd.read_parquet(DATASET)
df.reset_index(inplace=True, drop=True)

wb = app.books.open(WORKBOOK)
#sheet = wb.sheets["Emissions calculator"]
sheet = wb.sheets[SHEET]

emdata = []

for case in df.itertuples():
    sheet.range(MODEL).value = case.aircraft_type_icao
    sheet.range(AIRPORT).value = case.Airport
    sleep(0)
    emdata.append(sheet.range(LANDING if case.is_landing else TAKEOFF).value)
    sleep(0)
#cols = sheet.range(HEADERS).value
#cols = ['Mass of fuel burnt (kg)', 'Mass of CO emitted (kg)', 'Mass of HC emitted (kg)', 'Mass of NOX emitted (kg)', 'Mass of CO2 emitted (kg)', 'Mass of PMvol-org emitted (kg)', 'Mass of PMvol-sul emitted (kg)', 'Mass of PMnon-vol emitted (kg)', 'Mass of PMtotal emitted (kg)']

# Saving new data into dataframe
#print(sheet.range(HEADERS).value)
results = pd.concat([df, pd.DataFrame(emdata, columns=sheet.range(HEADERS).value)], axis=1)
print(results)
#print(emdata)
results.to_parquet(SAVE)

# Closing excel file
wb.close()
app.quit()
