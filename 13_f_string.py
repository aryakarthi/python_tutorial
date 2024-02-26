
# f-string

person = "Peter"
coins = 3

player = {'person': 'Tony', 'coins': 5}


def getcoins():
    return 6


coins_value = getcoins()


# using variables
message = f"\n{person} has {coins} coins left."
print(message)

# using function expression
message = f"\n{person} has {coins_value} coins left."
print(message)

# using built-in functions
message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

# using dictionary
message = f"\n{player['person']} has {5} coins left."
print(message)
