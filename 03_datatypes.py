import math

# string
greet = "Hello"
# greet = str("Hello") # using constructor
print(type(greet))
print(type(greet) == str)
print(isinstance(greet,str))

# concatenation
fname = "arya"
lname = "karthi"
fullname = fname + "" + lname
print(fullname)

greet += "!"
print(greet)

# type casting

# string to number
pin_str = "600017"
print(type(pin_str))
pincode = int(pin_str)
print(type(pincode))

# number to string
year = 2024
print(type(year))
newyear = str(year)
print(type(newyear))

# preserve intentation and spaces
intro = '''
   Python is an easy to learn, powerful programming language.

   It has efficient high-level data structures and a simple.

   But, effective approach to object-oriented programming.
'''

print(intro)

# escaping spl chars
sentence = 'It\'s raining!'
print(sentence)

# string methods
strvalue = "India wons the test series!"

print(strvalue.upper())
print(strvalue.lower())
print(strvalue.title()) # capitalize
print(strvalue.replace("test", "ODI")) # find and replace
print(len(strvalue))

print(len(intro))
print(len(intro.strip())) # trim whitespace
print(len(intro.lstrip())) # trim whitespace only from left
print(len(intro.rstrip())) # trim whitespace only from right

course = " MENU "
print(course.center(20,"="))

print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Tea".ljust(16, ".") + "$2".rjust(4))
print("Milk".ljust(16, ".") + "$1".rjust(4))

print(fullname) # returns aryakarthi
print(fullname[0]) # returns a
print(fullname[1]) # returns r
print(fullname[-1]) # returns i

print(fullname[0:4]) # returns arya
print(fullname[0:-6]) # returns arya
print(fullname[4:]) # returns karthi

print(fullname.startswith("a")) # returns True
print(fullname.endswith("a")) # returns False

# boolean

isalive = True
# isalive = bool(True) # using constructor
print(type(isalive))
print(type(isalive) == bool)
print(isinstance(isalive,bool))


# integers
price = 500
# price = int(300) # using constructor
print(type(price))
print(type(price) == int)
print(isinstance(price,int))

# float
tax = 2.28
# tax = float(2.25) # using constructor
print(type(tax))
print(type(tax) == float)
print(isinstance(tax,float))

# complex numbers
z = 5+2j
print(type(z))
print(z.real)
print(z.imag)

# number methods

print(abs(tax))
print(abs(tax * -1))
print(round(tax))
print(round(tax, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(tax))
print(math.floor(tax))