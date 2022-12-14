person = {"name" : "Marcos", "gender" : "Male", "address" : "Los Angeles", "phone": 664323121}

text = input ("What information do you want to know? ")

print(person.get(text,"Key not found"))