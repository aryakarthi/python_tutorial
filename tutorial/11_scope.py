
# scope

course = "Python"  # global scope


def greet(tutor):
    name = "Arya"  # local scope
    print("Hello " + name + "!")
    print("Welcome to the " + course + " tutorial!")
    print("Tutor: " + tutor)  # argument


greet("Dave Gray")

# nested functions


def circle():
    radius = 5
    color = "red"

    def circumference():

        # use nonlocal keyword to access local variable instead of global variable

        # nonlocal color
        # color = "blue"
        print(color)
        print(2*3.14*radius)
    circumference()

    def surface():
        print(3.14*radius**2)
    surface()


circle()


# global variable can only accessable, not modifiable

# use global keyword to modify global variables

count = 1


def increment():
    # count += 1  not modifiable
    global count
    count += 1
    print(count)


increment()
