
# # Class

class Student:
    name = "Tom"
    course = "Python"

    def description():
        print(f"{Student.name} is learning {Student.course}")


# create an instance
stud = Student()


print(type(Student))
print(type(stud))
print(isinstance(stud, Student))


# # Class Attributes

class User:
    name = "Tom"
    age = 23


# # to access the attributes

# 1 . getattr method


print(getattr(User, "name"))
print(getattr(User, "age"))
print(getattr(User, "city", "Not Available"))

# 2 . dot notation

print(User.name)
print(User.age)

# # to modify the attributes

# 1 . setattr method

setattr(User, "name", "Peter")  # updates existing attribute
print(User.name)
setattr(User, "gender", "Male")  # creates new attribute
print(User.gender)

# 2 . dot notation

User.age = 25  # updates existing attribute
print(User.age)
User.city = "Newyork"  # creates new attribute
print(User.city)

# to print all about the class

print(User.__dict__)

# # to remove an attribute

# 1 . delattr method

delattr(User, "gender")

# 2 . dot notation

del User.city

# to print all about the class

print(User.__dict__)

# # Instance Attributes


class Employee:
    company = "Microsoft"


# create an instance
emp = Employee()

print(Employee.__dict__)
print(Employee.company)  # prints class attribute

print(emp.__dict__)  # prints empty dictionary
print(emp.company)  # prints class attribute
emp.company = "Google"
print(emp.__dict__)
print(emp.company)  # prints instance attribute

print(Employee.company)  # class attribute is unchanged

# create another instance
emp2 = Employee()
print(emp2.company)  # prints class attribute


# # Class Methods

class Car:
    brand = "Nissan"
    model = "Magnite"
    color = "Red"

    def description():
        print(f"{Car.brand} {Car.model} is in {Car.color} color")


# prints class dictionary
print(Car.__dict__)

# to access class methods

# 1 . dot notation

Car.description()

# 2 . getattr method

# getattr(Car, "description")()

# 3 . using class dictionary

# Car.__dict__["description"]()


# # Instance Methods

class Mobile:
    brand = "Apple"
    model = "iPhone 13"

    def greet():
        print("Hello Everyone!")

    def description(self, color):
        print(f"{Mobile.brand} {Mobile.model} is in {color} color")


# create an instance
mob = Mobile()

# to access instance method
mob.greet()

# to add new attribute
mob.description("Black")
