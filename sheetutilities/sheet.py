import pygsheets

import os

path = os.getcwd()
print(path)
#client =pygsheets.authorize(service_account_file=f"{path}\\creds(3).json")
client =pygsheets.authorize(service_account_file=f"{path}\\sheetutilities\\creds(3).json")

spreadsheet =client.open("Truewaves")

def selectsheet(sheetname):
    global worksheet
    worksheet =spreadsheet.worksheet("title",f"{sheetname}")


def rowcount():
      a =worksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False,returnas ='matrix')

      rowcount =(len(a))
      return rowcount


def readdata(row):
    readdata =worksheet.get_value(f"{row}")
    return readdata


def writedata(row,column,data):
    writedata =worksheet.cell((row,column)).value =f"{data}"
    return  writedata



#selectsheet("Sheet1")
#a =readdata("A1")
#print(a)