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
