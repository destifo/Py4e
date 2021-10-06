import json

data = '''{
    "name" : "Estifanos",
     "phone" : {
        "type" : "intl",
        "number" : "+251 911 951 258"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
