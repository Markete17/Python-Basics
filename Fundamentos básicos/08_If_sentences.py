height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height * height))

if (bmi<18.5):
    print("Underweight")
elif (bmi>18.5 or bmi<=24.9):
    print("Normal weight")
elif (bmi>24.9 or bmi<=29.9):
    print("Overweight")
else:
    print("Obsesity")