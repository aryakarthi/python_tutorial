
# # dictionaries

user = {
    "name": "Peter",
    "email": "peter@gmail.com",
    "age": 23,
    "is_active": True,
}

# dict constructor

mobile = dict(brand="Apple", model="iPhone 13 Pro", price=79800)
print(mobile)

for i in mobile:
    print(str(i)+" : " + str(mobile[i]))

print("-"*30)

print(user)
print(type(user))

for i, j in user.items():
    print(str(i)+" : " + str(j))

print("-"*30)

# to access the items

print(user["name"])
print(user.get("email"))
print(user.keys())
print(user.values())
print(user.items())

# to check a item is exist or not

if "age" in user:
    print("Exists")
else:
    print("Not exist")

# to modify the dict/items

user.update({"gender": "Male"})
print(user)
user["age"] = 25
print(user)
user.pop("is_active")
print(user)

# to clear or delete dict

user.clear()
print(user)

# del user


# nested dictionary

contacts = {
    "contact1": {
        "name": "Peter",
        "mobile": "8796589875"
    },
    "contact2": {
        "name": "Tony",
        "mobile": "9858698659"
    },
    "contact3": {
        "name": "Steve",
        "mobile": "8965258954"
    }
}

print(contacts)
