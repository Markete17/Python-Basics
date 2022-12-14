# pip install requests
# pip install pprint ()


import requests
import json
import pprint

r = requests.get("https://opentdb.com/api.php?amount=1&category=19&difficulty=easy&type=multiple")
# print(r.status_code)
# print(r.headers)
# print(r.text)

print(r.status_code)
print(r.text)

questionJSON = json.loads(r.text) # de String a Dict
pprint.pprint(questionJSON)

category = questionJSON["results"][0]["category"]
print(category)

person = {"Name":"John","Age":30}
person_json = json.dumps(person) # Lo contrario a loads: de dictionary a String
print(person_json)