a = 20
b = 3

# arithmatic
print("arithmatic")
print(a+b)
print(a-b)
print(a*b)
print(a/b) # decimal
print(a//b) # rounds down
print(round(a/b)) # rounds up
print(a%b)
print(a**b)

# c = 99
# c+=1
# print(c)
# c-=2
# print(c)
# c*=3
# print(c)
# c/=4
# print(c)

print("")

# conditional
print("conditional")

x = 40
y = 22
print(x>y) # true
print(x>=y) # true
print(x==y) # false
print(x<y) # false
print(x<=y) # false
print(x!=y) # true
print("")

# boolean
print("boolean")
p=True
q=False

# and
print(p and p) # true
print(p and q) # false
print(q and q) # false

# or
print(p or p) # true
print(p or q) # true
print(q or q) # false

# not
print(not p) #false
print(not q) #true

#ternary
a, b = 10, 20
minimum = a if a < b else b
# [on_true] if [expression] else [on_false]
print("Minimum: ",minimum)  # Output: 10