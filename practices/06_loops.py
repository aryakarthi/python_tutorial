
# # while loop

# print even numbers between 1 and 10

# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# print("*"*30)

# print odd numbers between 1 and 10 using continue

# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# break

# i = 1
# while i <= 10:
#   print(i)
#   if i == 5:
#     break
#   i += 1


# # range - range(start,n-1,step)

# print(list(range(5)))
# print(list(range(2, 5)))
# print(list(range(1, 10, 2)))

# # for loop

# loop through the range

# for x in range(10):
#     print(x)

# loop through the string

# for x in "aryakarthi":
#     print(x)

# loop through the list

# days = ["Sunday", "Monday", "Tuesday", "Wednesday",
#         "Thursday", "Friday", "Saturday"]

# for x in days:
#     print(x)



# # nested for loop

for i in range(1,6):
  for j in range(i):
    print("*",end=" ")
  print("")

for i in range(5,0,-1):
  for j in range(i):
    print("*",end=" ")
  print("")



# # while else and for else
  
i=1
while i<5:
  if(i==3):
    print("Loop broken")
    break
  print(i)
  i+=1
else:
  print("Loop completed successfully")



for s in "aryakarthi":
  if s=="c": 
    print("loop broken")
    break
  print(s)
else:
  print("Loop completed successfully")