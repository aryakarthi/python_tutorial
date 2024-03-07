# Closure is a function having access to the scope of its parent
# function after the parent function has returned.

def player(person):
    coins = 5

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


tony = player("Tony")
peter = player("Peter")

tony()
tony()

peter()

tony()

peter()