import xlwings as wg
import pandas as pd
from time import sleep

# Files
LOAD = "./data_parsed/metadata.pq"
WORKBOOK = r".\main4.xlsm"
SHEET = "Emissions calculator"
SAVE = "./data_parsed/cruise{}-{}.pq"
SAVE_FLIGHTS = "./data_parsed/flights.pq"

# General parameters
MODEL = "C11"
CCD = "D21"
RESULTS = "G21:P21"
HEADERS = "G17:P17"
MODELS = ["A319", "B77W", "B772", "B738", "B38M", "A320", "A21N", "A321", "B789", "B788"]
REPLACEMENTS = {"A21N":"A321", "B38M":"B737"}
NM_TO_KM = 1.852
INTERCEPTS = [974.63,3070.12,34.36,0.83,1198.66,2.08,-0.03,-0.1542,-0.0491,-0.2028]
SLOPES = [6.05174,19.06296,0.08848,0.00508,7.44366,0.00714,0.00054,0.00166,0.0006372,0.002297]

# Excel setup
app = wg.App(visible=False, add_book=False)
app.screen_updating = False
wb = app.books.open(WORKBOOK)
sheet = wb.sheets[SHEET]

# Load files
flights = pd.read_parquet(LOAD, filters=[[("aircraft_type_icao", "==", model)] for model in MODELS])
flights.drop(['aircraft_engine_type',
       'origin_airport', 'origin_airport_name', 'origin_country',
       'destination_airport', 'destination_airport_name',
       'destination_country', 'scheduled_departure_time_utc',
       'scheduled_arrival_time_utc', 'first_waypoint_time',
       'last_waypoint_time', 'duration_hours',
       'great_circle_distance_km', 'longitude_first_waypoint',
       'longitude_last_waypoint', 'longitude_min', 'longitude_max',
       'latitude_first_waypoint', 'latitude_last_waypoint', 'latitude_min',     
       'latitude_max', 'altitude_first_waypoint', 'altitude_last_waypoint',     
       'altitude_min', 'altitude_max', 'n_wypts', 'n_terrestrial',
       'n_satellites', 'n_interpolate', 'n_extrapolate', 'n_great_circle',      
       'extrap_trajectory_start', 'extrap_trajectory_end',
       'trajectory_complete', 'great_circle_trajectory', 'est_origin_airport',  
       'est_destination_airport'], inplace=True, axis=1)
flights.reset_index(inplace=True, drop=True)
flights.replace({"aircraft_type_icao":REPLACEMENTS}, inplace=True)
flights["total_distance_nmi"] = flights["total_distance_km"]/NM_TO_KM
flights.to_parquet(SAVE_FLIGHTS)

emdata = []
start = 10000
c = 0
end = 20000

for i in flights.itertuples():
    if c < start:
        c += 1
        continue
    if c >= end:
        break
    
    if c%50 == 0:
        print(c)
    
    if i.aircraft_type_icao == "A321" and i.total_distance_nmi >= 2500:
        print("interp")
        emdata.append([INTERCEPTS[j]+SLOPES[j]*i.total_distance_nmi for j in range(10)])
    else:
        sheet.range(MODEL).value = i.aircraft_type_icao
        sleep(0)
        emdata.append(sheet.range(RESULTS).value)
        sleep(0)
    c += 1

# Saving new data into dataframe
results = pd.DataFrame(emdata, columns=sheet.range(HEADERS).value)
print(results)
results.to_parquet(SAVE.format(start, end))

# Closing excel file
wb.close()
app.quit()