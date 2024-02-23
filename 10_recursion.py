
# # recursion

# @ simple increment function using recursion
def add_one(num):

    if (num >= 9):
        return num + 1
    else:
        total = num + 1
        print(total)

    return add_one(total)


mynewtotal = add_one(5)
print(mynewtotal)


# @ find factorial of the number
def factorial(n, a=1):
    if n == 0:
        return a
    else:
        return factorial(n - 1, n * a)


get_factorial = factorial(5)
print(get_factorial)
