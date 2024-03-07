avengers = ["Ironman","Spiderman","Thor","Hulk","Captain America"]

data = ["Jarvis", 3000, True, 2.0]

empty_list = []

print("Ironman" in avengers) # True
print("Ironman" in data) # False
print("Ironman" in empty_list) # False

print(avengers[0])
print(avengers[-1])

print(avengers.index('Hulk'))

print(avengers[0:2])
print(avengers[3:])
print(avengers[-3:-1])

print(len(avengers))

# add item to the list
# append
avengers.append('Hawkeye')

# concat
avengers += ['Black Widow']

# extend
avengers.extend(['Black Panther'])

# insert
avengers.insert(0, 'Doctor Strange')

# add items to the specific position in the list
avengers[2:2] = ['Wanda', 'Vision']

# replace existing list items with new one
# avengers[2:4] = ['Nebula', 'Groot']

print(avengers)

# remove item from the list
# avengers.remove('Doctor Strange')

# remove last item from the list
# print(avengers.pop())

# remove specific item from the list
# del avengers[1:3]

# to delete the list
# del avengers

# to empty the list
# avengers.clear()

# sorting the list items

# add item in lowercase
avengers[2:3] = ['antman']

# sort method is case in-sensitive.
avengers.sort()
print(avengers)

# use key to sort the list items (all items should be in same datatype)
avengers.sort(key=str.lower)

print(avengers)

# sort number list

nums = [9, 67, 38, 13, 24, 49, 56]

# using sorted method

# descending
print(sorted(nums, reverse=False))

# ascending
print(sorted(nums, reverse=True))

# sorted method doesn't modify original list
print(nums)

# reverse the list items
nums.reverse()
print(nums)


# using sort method

# ascending
nums.sort()
print(nums)

# descending
nums.sort(reverse=True)
print(nums)

# copy the list items
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print(days)

print(type(days))

# copy method
dayscopy1 = days.copy()
print(dayscopy1)

# constructor method
dayscopy2 = list(days)
print(dayscopy2)

# using list index
dayscopy3 = days[:]
print(dayscopy3)


# Tuples - can have multiple datatypes of items and those items cannot be modified.

user1 = ('Steve', 35, False, 3.452)
print(user1)
print(type(user1))

# using constructor
user2 = tuple(('Tony', 45, True, 2.342))
print(user2)
print(type(user2))

# to copy the tuple

# convert tuple into list
new_userlist = list(user1)
print(new_userlist)

# add new list item to that list
new_userlist.append('Jobs')

# again convert that list into tuple
new_usertuple = tuple(new_userlist)
print(new_usertuple)


# unpacking tuple (like destructuring)

(first, second, *rest) = user2
print(first)
print(second)
print(rest)

months = ("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec")

(firstmonth, *mid, lastmonth) = months
print(firstmonth)
print(mid)
print(lastmonth)


