import json


with open("person.json", "r", encoding="utf-8") as file:
   
    data = json.load(file)


    print(data)
