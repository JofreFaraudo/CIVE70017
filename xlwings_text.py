import xlwings as wg

app = wg.App(visible=True, add_book=False)
app.screen_updating = False

wb = app.books.open(r"C:\Users\jf2326\OneDrive - Imperial College London\Documents\lto.xlsm")
#sheet = wb.sheets["Emissions calculator"]
sheet = wb.sheets["LTO emissions calculator"]

print("{}: {}".format(sheet.range("F26").value, sheet.range("G40").value))
sheet.range("F26").value = 2015
print("{}: {}".format(sheet.range("F26").value, sheet.range("G40").value))
sheet.range("F26").value = 2019
print("{}: {}".format(sheet.range("F26").value, sheet.range("G40").value))

wb.close()
app.quit()
