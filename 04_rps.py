import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


playagain = True
while playagain:

    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    pythonchoice = random.choice("123")

    python = int(pythonchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(python)).replace('RPS.', '') + ".\n")

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

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thanks for playing!\n")
        playagain = False

sys.exit("Bye! 👋")
