import xlwings as wg
import pandas as pd
from time import sleep

# Files
WORKBOOK = r".\lto3.xlsm"
SHEET = "LTO emissions calculator"
DATASET = "./data_parsed/LTO.pq"
SAVE = "./data_parsed/LTOfix.pq"

# Parameters
MODEL = "F14"
# SET AIRPORT MANUALLY TO 'OTHER' FOR BEST PERFORMANCE
HEADERS = "C40:C48"
TAKEOFF = "V40:V48"
LANDING = "AK40:AK48"
MODELS = ['A319   (Airbus A-319) with CFM56-5B5/P engines ***', 'B77W   (Boeing 777-300ER) with GE90-115B engines ***', 'B772   (Boeing 777-200) with GE90-94B engines ***', 'B738   (Boeing 737-800) with CFM56-7B26 engines ***', 'B38M   (Boeing 737 Max 8)', 'A320   (Airbus A-320) with CFM56-5B4/P engines', 'A21N   (Airbus A-321 NEO) with LEAP-1A32 engines ***', 'A321   (Airbus A-321) with V2533-A5 engines ***', 'B789   (Boeing 787-9 Dreamliner) with GEnx-1B64 engines', 'B788   (Boeing 787-8 Dreamliner) with GEnx-1B64 engines ***']

# Excel setup
app = wg.App(visible=False, add_book=False)
app.screen_updating = False

# Opening files
df = pd.read_parquet(DATASET)
df.reset_index(inplace=True, drop=True)

wb = app.books.open(WORKBOOK)
sheet = wb.sheets[SHEET]

# Retrieve data
cols = sheet.range(HEADERS).value
sleep(0)
reference = [{},{}] # 0: Take-offs, 1: Landings
op = 0
while op < 2:
    for model in MODELS:
        sheet.range(MODEL).value = model
        sleep(0)
        reference[op][model] = sheet.range(LANDING if op else TAKEOFF).value
        sleep(0)
    op += 1

# Closing excel file
wb.close()
app.quit()
print(reference)

# Updating df
null_df = df[df["Mass of fuel burnt (kg)"].isnull()]
for case in null_df.itertuples():
    i = 0
    while i < len(cols):
        df.at[case.Index, cols[i]] = reference[int(case.is_landing)][case.aircraft_type_icao][i]
        i += 1

print(df)
df.to_parquet(SAVE)