print("Exercise: Km to Miles Converter")

number_km = float(input("Please enter the km to convert it in miles:"))
MILES_CONST = 1.609344

number_miles = round(number_km / MILES_CONST,4)

print(number_km,"km is",number_miles,"miles")
