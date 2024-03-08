
# # lists

n = [1, 2, 3, 4, 5]

print(n)
print(type(n))
print(len(n))

# constructor

p = list([10, 11, 12, 13, 14, 15])
q = list(["hello", 25, 6.8, True])
r = list(range(5))
s = list("aryakarthi")


# # list slicing

print(n)  # [1, 2, 3, 4, 5]
print(n[1])  # 2
print(n[1:3])  # [2, 3]
print(n[1:])  # [2, 3, 4, 5]
print(n[:3])  # [1, 2, 3]
print(n[-1])  # 5
print(n[-3:-1])  # [3, 4]
print(n[:-1])  # [1, 2, 3, 4]
print(n[-3:])  # [3, 4, 5]

# # methods

nums = [10, 20, 30, 30, 30, 40, 50]

print(nums.count(30))
print(nums.index(40))
print(min(nums))
print(max(nums))

x = nums.copy()
print(x)
print(x.pop())
print(x.pop(2))

x.remove(30)
print(x)

x.clear()
print(x)

super_heroes = ["iron man", "thor", "captain america", "hulk"]

super_heroes.append("spider man")
print(super_heroes)

dc = ["bat man", "super man", "wonder woman"]
dc.insert(2, "aqua man")
print(dc)

super_heroes.extend(dc)
print(super_heroes)


# sorting list

super_heroes.sort()
print(super_heroes)

super_heroes.sort(reverse=True)
print(super_heroes)

super_heroes.sort(key=len)
print(super_heroes)

digits = [67, 89, 72, 94, 58, 45, 29, 36]
print(digits)

digits.sort()
print(digits)

digits.sort(reverse=True)
print(digits)
