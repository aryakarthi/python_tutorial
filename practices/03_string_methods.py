
# # string methods

quote = "Well done is better than Well said!"
print(quote, type(quote))

print(quote.upper()) # to uppercase
print(quote.lower()) # to lowercase
print(quote.capitalize()) # captitalize the first word
print(quote.title()) # captitalize the each words
print(quote.count("e")) # counts only lower 'e'
print(quote.endswith("said!")) # returns True
print(quote.find("e")) # returns index 
print(quote.find("e",2)) # returns index after 2nd index
print(quote.find("u")) # returns -1 if not found
print(quote.replace("o","0")) # replaces 'o' with '0'
print(quote.split())

fname = "arya25"
print(fname)
print("is upper : ",fname.isupper()) # returns False
print("is lower : ",fname.islower()) # returns True
print("is alpha numeric : ",fname.isalnum()) # returns True
print("is alpha : ",fname.isalpha()) # returns True

q = "DREAM\nBELIEVE\nACHIEVE"

print(q.splitlines()) # returns ['DREAM', 'BELIEVE', 'ACHIEVE']
print(q.splitlines(True))

d = "26-11-1993"
print(d.split("-")) # returns ['26', '11', '1993']
print(d.partition("-")) # returns ('26', '-', '11-1993')
# partition returns (all before match, match, all after match)

# # string manipulation

name = "aryakarthi"
# name[start, no of chars]
print(name)
print(name[0:4]) # arya
print(name[:4]) # arya
print(name[4:]) # karthi
print(name[-1]) # i
print(name[-5:-2]) # art
print(name[:-3]) # aryakar
print(name[::-1]) # ihtrakayra