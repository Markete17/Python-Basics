import random
names_list = []
colors = ["blue","red","purple","yellow","green","orange"]
random_index = random.randint(0,len(colors)-1)
while(len(names_list)<8):
    name = input("Enter a name: ")
    names_list.append(name)
random_index = random.randint(0,len(names_list)-1)
print(names_list[random_index])

user_color=""
while (user_color!="no"):
    random_index = random.randint(0,len(colors)-1)
    color = colors[random_index]
    user_color = input ("Write a color. Write no to exit: ") #A minusculas
    if(user_color==color):
        print("Correct!")
        break
    elif(user_color!="no" and user_color!=color):
        print("Incorrect")
    else: print("Exiting...")
