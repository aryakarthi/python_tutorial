
# # OPERATORS

# # arithmatic
a = 33
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # returns 16.5 - division
print(a//b)  # returns 16 - floor division
print(a % b)
print(a**b)

# # comparision
print(a == b)  # returns False
print(a != b)  # returns True
print(a < b)  # returns False
print(a <= b)  # returns False
print(a > b)  # returns True
print(a >= b)  # returns True

# # logical
print(a != b and a > b)  # returns True
print(a == b and a < b)  # returns False
print(a == b or a > b)  # returns True
print(a == b and a < b)  # returns False
print(not (a == b and a < b))  # returns True

# # bitwise
print(a & b)  # and
print(a | b)  # or
print(a ^ b)  # xor
print(~b)  # not
print(b << 2)  # zero fill left shift
print(b >> 2)  # signed right shift

# # identity operators

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(c))
print(id(a))
print(id(b))

print(a == b)  # returns True.
# Bcos, elements in both lists are same.

print(a is b)  # returns False.
# Bcos, only elements in both lists are same. But, memory addresses are different.

print(a is c)  # returns True.
# Bcos, elements in both lists and memory addresses of both lists are same.

# vise-versa

print(a != b)  # returns False
print(a is not b) # returns True
print(a is not c) # returns False

# # membership operators

fruits = ["apple", "orange", "mango", "banana"]
print(fruits)
print("apple" in fruits) # returns True
print("orange" not in fruits) # returns False
