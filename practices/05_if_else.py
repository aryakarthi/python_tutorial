
# # if statement

# num = 8
# if num & num-1 == 0:
#     print(str(num)+" is Power of 2")

# # if else statement

# num = 10
# if num & num-1 == 0:
#     print(str(num) + " is Power of 2")
# else:
#     print(str(num) + " is not Power of 2")

# # if elif statement

# amount = 100
# days = 47

# if days == 0:
#     print("No fine")
# elif days > 0 and days <= 10:
#     fine = amount*0.2
#     print(fine)
# elif days > 10 and days <= 30:
#     fine = amount*0.5
#     print(fine)
# elif days > 30:
#     fine = amount*0.7
#     print(fine)
# else:
#     print("Enter valid days")


# # nested if statement

mat = int(input("Maths marks : "))
phy = int(input("Physics marks : "))
che = int(input("Chemistry marks : "))

total = mat+phy+che
aveg = total/3

if mat >= 35 and phy >= 35 and che >= 35:
    print("Total : " + str(total))
    print("Average : " + str(aveg))
    print("Result : Pass")
    if aveg >= 90 and aveg <= 100:
        print("Grade : A")
    elif aveg >= 80 and aveg < 90:
        print("Grade : B")
    elif aveg >= 70 and aveg < 80:
        print("Grade : C")
    elif aveg >= 60 and aveg < 70:
        print("Grade : D")
    else:
        print("Grade : E")
else:
    print("Result : Fail")
