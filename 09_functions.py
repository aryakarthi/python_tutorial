# functions

# simple function
def hello_world():
    print("Hello world!")


hello_world()

# add function with args


def add(n1, n2):
    print(n1+n2)


add(2, 3)

# sum function with default args


def sum(n1=0, n2=0):
    if (type(n1) is not int or type(n2) is not int):
        return 0
    return n1 + n2


total = sum(7, 2)
print(total)
total = sum("7", 2)
print(total)

# args 
def display_students(*args):
    print(args)
    print(type(args))


display_students("Michelle", "Peter", "Ned")

# kwargs - keyword arguments
def mark_list(**kwargs):
    print(kwargs)
    print(type(kwargs))


mark_list(maths=89, physics=82, chemistry=79)
