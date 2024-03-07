import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        def decide_winner(player, python):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and python == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and python == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and python == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == python:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, python)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

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

    return play_rps


play = rps()

play()
