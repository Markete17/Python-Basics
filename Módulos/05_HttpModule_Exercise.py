from unicodedata import category
import requests
import json
import pprint
import random
import html

answer = ""

# https://opentdb.com/api.php?amount=1&category=32&difficulty=easy&type=multiple
# amount = 1
# category = [0,32]
# difficulty = easy,medium,hard
# type = multiple,boolean

difficulties = ["easy","medium","hard"]
types = ["multiple","boolean"]

while(answer != "quit"):

    r = requests.get("https://opentdb.com/api.php?amount=1")
    if(r.status_code != 200):
        answer = input("Sorry, there was a problem. Press enter to try again or 'quit' to quit the game")
    else:
        data = json.loads(r.text)

        question = data["results"][0]["question"]
        category = data["results"][0]["category"]
        answers = data["results"][0]["incorrect_answers"]
        correct = data["results"][0]["correct_answer"]
        answers.append(correct)
        random.shuffle(answers)

        
        print("Question [Category] = "+category+"\n")
        print(html.unescape(question)) # convierte el contenido html en una cadena
        print("ANSWERS:\n")
        for index,value in enumerate(answers):
            print(index+1,html.unescape(value))
        user_answer = int(input("Type the number of your answer: "))
        if(answers[user_answer-1] == correct):
            print("CORRECT!\n")
        else:
            print("INCORRECT!\n")
        answer = input("Do you want to exit? write 'quit' to exit: ")
print("\n")
print("Exiting")