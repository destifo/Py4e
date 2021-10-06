import json

data = '''[
    {
        "name" : "Estifanos",
        "id" : "009",
        "x" : "17"
    },
    {
        "name" : "Ezra",
        "id" : "007",
        "x" : "16"
    }
]'''

info = json.loads(data)
for item in info:
    print('Name:', item["name"])
    print('id:', item["id"])
    print('Attribute:', item["x"])
