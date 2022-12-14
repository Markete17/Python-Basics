import math
radius = float(input("Please enter the area: "))

area = math.pi * math.pow(radius,2)
circumference = 2 * math.pi * radius

print("Area:",round(area,2))
print("Circumference:",round(circumference,2))
