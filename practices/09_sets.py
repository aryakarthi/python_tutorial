
# # sets
# - remove duplicates
# - unordered unindexed datatypes

names = {"peter", "tony", "peter"}
print(names)

# adding element

names.add("steve")
print(names)

# adding set

w = {"pepper", "peggy", "mj", "wanda"}
names.update(w)
print(names)

# removing element

names.remove("wanda")
print(names)

names.pop()  # remove any one element
print(names)

# discord - if element exists remove, else discorded

# names.discard("wanda")
# print(names)

# clear and delete set
names.clear()
print(names)

# del names

# merging sets

p = {1, 2, 3, 4}
q = {2, 4, 6, 8}

n = p.union(q)
print(n)

p.update(q)
print(p)

# Keeps only the duplicates

a = {1, 2, 3, 4}
b = {2, 4, 6, 8}

n = a.intersection(b)
print(n)

a.intersection_update(b)
print(a)

# Keeps everything except the duplicates

x = {1, 2, 3, 4}
y = {2, 4, 6, 8}

n = x.symmetric_difference(y)
print(n)

x.symmetric_difference_update(y)
print(x)
