
# # tuples - immutable

my_tuple = ("hi", 100, 3.14, False, [1, 2, 3])
print(my_tuple)

# constructor

r = tuple(range(5))
s = tuple("aryakarthi")
tc = tuple((10, 20, 30, 40, 50))


t = (1, 2, 3, 4, 5)
print(t)
print(type(t))

# # tuple slicing

print(t)  # (1, 2, 3, 4, 5)
print(t[1])  # 2
print(t[1:3])  # (2, 3)
print(t[1:])  # (2, 3, 4, 5)
print(t[:3])  # (1, 2, 3)
print(t[-1])  # 5
print(t[-3:-1])  # (3, 4)
print(t[:-1])  # (1, 2, 3, 4)
print(t[-3:])  # (3, 4, 5)


# to modify tuple, change tuple as list

print(t)  # (1, 2, 3, 4, 5)
tl = list(t)
print(tl)  # [1, 2, 3, 4, 5]
tl.append(6)
print(tl)  # [1, 2, 3, 4, 5, 6]
t = tuple(tl)
print(t)  # (1, 2, 3, 4, 5, 6)

# to iterate tuple

for i in t:
    print(i)

# to check element in tuple

print(s)
if "c" in s:
    print("Found!")
else:
    print("Not found!")

x = ("arya")  # string
print(x, type(x))
x = ("arya",)  # tuple
print(x, type(x))

a = (2, 3, 4)
b = (4, 5, 6)
c = a+b
print(c)  # (2, 3, 4, 4, 5, 6)
print(c.count(4))  # 2
print(min(c))  # 2
print(max(c))  # 6

d = (a, b)
print(d)  # ((2, 3, 4), (4, 5, 6))

repeat = ("arya",)*3
print(repeat, type(repeat))
