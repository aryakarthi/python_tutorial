# Dictionaries (like objects in js)

user = {
    "name": "Steve",
    "email": "steve@example.com",
    "mobile": "8745896589",
    "city": "New York",
}
print(user)
print(type(user))
print(len(user))

student = dict(name="Peter", age=20, department="CSE", gpa=6.45)
print(student)
print(type(student))
print(len(student))

# access dictionary items

# bracket notation
print(user["name"])

# get method
print(user.get("mobile"))


# list all keys in dictionary
print(user.keys())

# list all values in dictionary
print(user.values())

# list of key/value pairs as tuples
print(user.items())


# verify a key exists
print("name" in user)
print("email" in student)


# modify values in dictionary
user["city"] = "Brooklyn"
student.update({"age": 19})

print(user)
print(student)


# remove items

# pop - remove specific item from dictionary
print(student.pop("age"))
print(student)

# popitem - remove last item from dictionary, returns a tuple
print(student.popitem())
print(student)

# to delete specific item from dictionary
del user["city"]
print(user)


# clear and delete dictionary

# clear all values in dictionary
student.clear()
print(student)

# delete the dictionary
del student


# Copy dictionaries

# this method modify the original dictionary too
# user2 = user
# print(user2)
# print(user)

# user2["city"] = "Paris"
# print(user2)
# print(user)

# these methods will not modify the original dictionary

# copy method
user3 = user.copy()
print(user3)
print(user)

user3["zipcode"] = "854475"
print(user3)
print(user)

# constructor method
user4 = dict(user)
print(user4)


# Nested dictionaries

mobile1 = {
    "brand": "Samsung",
    "model": "S22 Ultra",
    "price": 70000
}
mobile2 = {
    "brand": "iPhone",
    "model": "13 Pro Max",
    "price": 80000
}

mobiles = {
    "mobile1": mobile1,
    "mobile2": mobile2
}

print(mobiles)

# access item in nested dictionary
print(mobiles["mobile1"]["brand"])