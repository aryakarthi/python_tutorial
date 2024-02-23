import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

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

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thanks for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
