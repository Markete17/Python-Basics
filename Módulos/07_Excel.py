# pip install pandas
# pip install xlrd
# pip install openpyxl

import pandas as pd
file = pd.ExcelFile("C:/Users/mruiz/Desktop/python/excel.xlsx")
print(file.sheet_names)
print("\n")
sheet = file.parse("Hoja1")
print(type(sheet))
print("\n")

print(sheet.Date) #Imprime el valor de la columna Date
print("\n")

print(sheet.Amount) 
print("\n")
print(sheet.Amount.sum()) # Sumar los valores de la columna

print("\n")
print(sheet.loc[0]) #Imprime los valores de la línea
print("\n")
print(sheet.loc[0]['Amount']) #De la primera linea 0, imprimir solo el campo Amount
print("\n")

# Buscar registros dependiendo valores
sheet.set_index("Customer",inplace=True) #Asignar indice a columna
print(sheet.loc["MMC Inc."])
sheet = sheet.reset_index() # Resetear indices
print("\n")

print(sheet.loc[sheet["Invoice"] == 99]) #Imprimir la línea en el que tenga un invoice=99
print("\n")
print(sheet.loc[sheet["Amount"].idxmax()]) #Imprime la línea del customer que tenga mayor amount
print("\n")
print(sheet.loc[sheet["Amount"].idxmax()]["Customer"]) 
print("\n")
print(sheet.loc[sheet["Amount"]>2000]["Customer"].unique()) 