
# # DATA TYPES

# # string
name = "peter"
print(name)
print(type(name))

# # integer
age = 25
print(age)
print(type(age))

# # boolean
is_active = True
print(is_active)
print(type(is_active))

# # float
gpa = 8.2
print(gpa)
print(type(gpa))

# # complex
x = 3+4j
print(x)
print(type(x))

# # list
fruits = ["apple", "orange", "mango"]
print(fruits)
print(type(fruits))

# # tuple
pets = ("dog", "cat", "parrot", "dove")
print(pets)
print(type(pets))

# # set
directions = {"north", "south", "east", "west"}
print(directions)
print(type(directions))

# # dictionary
mobile = {
    "brand": "Samsung",
    "model": "S23",
    "year": 2023
}
print(mobile)
print(type(mobile))

# # range
numbers = range(5)
print(numbers)
print(type(numbers))

# # TYPE CASTING

# # str to int
num = "3000"
print(num, type(num))
num = int(num)
print(num, type(num))

# # int to str
digit = 7
print(digit, type(digit))
digit = str(digit)
print(digit, type(digit))

# # list to tuple
birds = ["duck", "parrot", "dove"]
print(birds, type(birds))
birds = tuple(birds)
print(birds, type(birds))

# # tuple to list
prod = (1, "parrot", True, 3.5)
print(prod, type(prod))
prod = list(prod)
print(prod, type(prod))

# # list to set
integers = [1,1,2,3,4,4,5,5]
print(integers, type(integers))
integers = set(integers)
print(integers, type(integers))