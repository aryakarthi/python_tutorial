from functools import reduce

# lambda

# using single arguments


def square(num): return num**2


print(square(7))

# using two arguments


def sum(a, b): return a + b


print(sum(10, 16))


# higher order functions

numbers = [13, 5, 7, 9, 4, 8]

# map
squared_nums = map(lambda num: num * num, numbers)

print(type(squared_nums))
print(list(squared_nums))

# filter
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(type(odd_nums))
print(list(odd_nums))


# reduc
nums = [1, 2, 3, 4, 5]

total = reduce(lambda acc, curr: acc + curr, nums, 0)

print(total)
