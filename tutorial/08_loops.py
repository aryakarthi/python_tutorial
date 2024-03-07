# while loop

value = 100
while value <= 110:
  print(value)
  value += 1

# breaks at 5

# value = 1
# while value <= 10:
#   print(value)
#   if value == 5:
#     break
#   value += 1


# skips 5

# value = 0
# while value < 10:
#     value += 1
#     if value == 5:
#         print("Skipped "+ str(value))
#         continue
#     else:
#      print(value)


# for loop

# loop through the string
for x in "Mississippi":
    print(x)

# loop through the list
avengers = ["Ironman", "Spiderman", "Thor", "Hulk",
            "Captain America", "Hawkeye", "Black Widow"]

for x in avengers:
    print(x)

# breaks loop at value "Thor"

# for x in avengers:
#     if x == "Thor":
#         break
#     print(x)

# skips the value "Thor"

# for x in avengers:
#     if x == "Thor":
#         continue
#     print(x)


# range in for loop

# prints 0 to 9
    
for x in range(10):
    print(x)

# prints from 3 to 9 (start, end before)
    
# for x in range(3, 10):
#     print(x)

# prints from 3 to 31, increments by 3
    
# for x in range(3, 31, 3):
#     print(x)
    
# nested for loop
    
names = ["Tony", "Peter", "Jarvis"]
actions = ["eats", "codes", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")
