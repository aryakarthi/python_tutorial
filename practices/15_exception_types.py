
# # Types of Exceeption

# # NameError exception

# try:
#     print(s)
# except NameError as e:
#     print(e)
#     print("Value is not defined!")

# # ZeroDivisionError exception

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)
#     print("Denominator should not be zero!")

# # ValueError exception

# try:
#     n = int("One")
# except ValueError as e:
#     print(e)
#     print("Invalid number")

# # IndexError exception

# try:
#     nums = [1, 2, 3, 4, 5]
#     print(nums[10])
# except IndexError as e:
#     print(e)
#     print("Invalid number")

# # FileNotFoundError exception

# try:
#     file = open("sample.txt")
# except FileNotFoundError as e:
#     print(e)
#     print("File not found!")

# # handling multiple exceptions

try:
    a = 10/0
    print(a[0])
except ZeroDivisionError:
    print("Denominator shouldn't be zero!")
except TypeError:
    print("Invalid Date Type!")
else:
    print(a)
finally:
    print("Completed!")
