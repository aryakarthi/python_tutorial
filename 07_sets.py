# Sets
# - removes duplicates.
# - cannot access items using index or key in set

# create a new set
marks = {81, 92, 73, 84, 79}
print(marks)
print(type(marks))
print(len(marks))

marks2 = set((71, 82, 93, 74, 89))

print(marks2)
print(type(marks2))
print(len(marks2))


# duplicates not allowed
marks3 = {81, 81, 73, 81, 79}
print(marks3)

# True as 1, False as 0
nums = {0, False, 1, True, 2, 3, 4, 0, 1}
print(nums)

# if True/False is comes first before 0/1, it returns True/False
num2 = {False, 0, True, 1, 2, 3, 4, 0, 1}
print(num2)

# check if a value is in a set
print(2 in nums)  # returns True


# Add a new element to a set

# add method
nums.add(5)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# Merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
