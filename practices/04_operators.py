
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
print(not(a == b and a < b))  # returns True

# # bitwise
print(a&b) # and
print(a|b) # or
print(a^b) # xor
print(~b) # not
print(b<<2) # zero fill left shift
print(b>>2) # signed right shift
