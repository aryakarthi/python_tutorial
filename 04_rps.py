import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

pythonchoice = random.choice("123")

python = int(pythonchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(python)).replace('RPS.', '') + ".")
print("")

if player == 1 and python == 3:
    print("🎉 You win!")
elif player == 2 and python == 1:
    print("🎉 You win!")
elif player == 3 and python == 2:
    print("🎉 You win!")
elif player == python:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")