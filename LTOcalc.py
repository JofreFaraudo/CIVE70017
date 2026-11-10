import xlwings as wg
import pandas as pd

# Files
DATASET = "./data_parsed/operations.pq"
WORKBOOK = r".\lto.xlsm"
SHEET = "LTO emissions calculator"

# Sheets parameters
MODEL = "F14"
AIRPORT = "F24"
TAKEOFF = "V40:V48"
LANDING = "AO40:AO48"
HEADERS = "C40:C48"

# Excel setup
app = wg.App(visible=True, add_book=False)
app.screen_updating = False

# Opening files
df = pd.read_parquet(DATASET)
wb = app.books.open(WORKBOOK)
#sheet = wb.sheets["Emissions calculator"]
sheet = wb.sheets[SHEET]

emdata = []

for case in df.itertuples():
    sheet.range(MODEL).value = case.aircraft_type_icao
    sheet.range(AIRPORT).value = case.Airport
    emdata.append(sheet.range(LANDING if case.is_landing else TAKEOFF).value)

# Saving new data into dataframe
results = pd.concat([df, pd.DataFrame(emdata, columns=sheet.range(HEADERS).value)], axis=1)
print(results)

# Closing excel file
wb.close()
app.quit()
