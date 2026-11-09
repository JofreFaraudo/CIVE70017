import xlwings as wg

app = wg.App(visible=True, add_book=False)
app.screen_updating = False

wb = app.books.open(r".\lto.xlsm")
#sheet = wb.sheets["Emissions calculator"]
sheet = wb.sheets["LTO emissions calculator"]

"""
# Any
print("{}: {}".format(sheet.range("F26").value, sheet.range("G40").value))
sheet.range("F26").value = 2015
print("{}: {}".format(sheet.range("F26").value, sheet.range("G40").value))
sheet.range("F26").value = 2019
print("{}: {}".format(sheet.range("F26").value, sheet.range("G40").value))

# Aero icao codi
print("{}: {}".format(sheet.range("F24").value, sheet.range("G40").value))
sheet.range("F24").value = "EGLL"
print("{}: {}; 7.8040".format(sheet.range("F24").value, sheet.range("G40").value))
sheet.range("F24").value = "EGGP"
print("{}: {}; 4.1177".format(sheet.range("F24").value, sheet.range("G40").value))
"""

# Model avio
print("{}: {}".format(sheet.range("F14").value, sheet.range("G40").value))
sheet.range("F14").value = "A310   (Airbus A-310) with PW4156 engines"
print("{}: {}".format(sheet.range("F14").value, sheet.range("G40").value))

wb.close()
app.quit()
