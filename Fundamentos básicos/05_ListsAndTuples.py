months = ("January","February","March","April","May","June","July","August","September","October","November","December")

text = input("Print your birthday in this format 'DD-MM-YYYY': ")

month = int(text[3:5])

print("You were born in",months[month-1])

persons = ["Marcos","Julian","Maria"]

name = input ("Please, enter your name: ")

persons.append(name)

print("list:",persons)
