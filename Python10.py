"""
#
# Part : python JSON
#API
"""

import json

# make a json
x = '{"name": "John" , "age": "20", "city": "Phuket"}'

# parse x
y =json.loads(x)

#Python Dictionry
print(y)
print(y["city"])

#Python Dictionry
a = {
    "name": "John",
    "age": "20",
    "city":"Phiket"
}

# convert into JSON (string)
b = json.dumps(a)

# JSON string
print(b)