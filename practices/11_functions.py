
# # functions

# no return and without arguments functions


def add():
    a, b = 10, 20
    c = a+b
    print(c)


add()

# no return and with arguments functions


def sub(a, b):
    c = a-b
    print(c)


sub(10, 2)

# return and without arguments functions


def mul():
    a, b = 10, 2
    c = a*b
    return c


m = mul()
print(m)

# return and with arguments functions


def div(a, b):
    c = a/b
    return c


d = div(10, 2)
print(d)

# arbitary argument functions (*)


def getmarks(*marks):
    print(marks)


getmarks(78, 89, 84, 73, 79)  # retuns (78, 89, 84, 73, 79)

# keyword arguments functions


def msg(name, age):
    print(str(name) + " is " + str(age) + " years old!")


msg(age=23, name="Peter")

# arbitary keyword arguments functions (**)


def getcontact(**contact):
    print(contact)


# returns {'name': 'Tony', 'email': 'tony@gmail.com', 'city': 'Newyork'}
getcontact(name="Tony", email="tony@gmail.com", city="Newyork")

# default parameter functions


def getinfo(name, city="Chennai"):
    print(str(name) + " is from " + str(city))


getinfo("Tony", "Newyork")
getinfo("Vijay")

# passing a list as an argument in functions


def total(marks):
    return sum(marks)


t = total([78, 89, 84, 73, 79])
print(t)

# recursive function


def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))


f = factorial(5)
print(f)

# lambda functions


# square = lambda n:n**2
def square(n): return n**2


print(square(5))
