#!/usr/bin/python3
# Rock paper scissors game, w/o ASCII.
# With a score counter too!
# Sure this could probably benefit from using case but that would be down the line...
import random
import sys

player_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors ultimate showdown 3000!")

play = input("Wanna play? [y/n]")

if play.lower() == "y":
    while play.lower() == "y":

        player_choice = input(
            "Choose your battlestance:\n 0 for rock, 1 for paper, 2 for scissors: \n")
        # Break if player is dumb and didn't choose possible number...
        # Can be upgraded to only accept integers with some secondary loop possibly.
        if int(player_choice) > 2:
            print(f"This isn't rock paper shotgun!")
            break

        computer_choice = random.randint(0, 2)
        pchoice_as_string = options[int(player_choice)]
        cchoice_as_string = options[computer_choice]

        if int(player_choice) == computer_choice:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print(f"Theese look the same...")
            print("...")
            print("...draw...")

        elif int(player_choice) == 0 and computer_choice == 2:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print("ROCK SMASHES! Fatality!")
            player_score += 1
        elif int(player_choice) == 0 and computer_choice == 1:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print("Stealthy paper covers rock... COMPUTER WINS!")
            computer_score += 1
        elif int(player_choice) == 1 and computer_choice == 0:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print("Stealthy paper covers rock... PLAYER WINS! Flawless victory!")
            player_score += 1
        elif int(player_choice) == 1 and computer_choice == 2:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print("Death, by a thousand paper cuts! Computer wins!")
            computer_score += 1
        elif int(player_choice) == 2 and computer_choice == 0:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print("They should've told you not to run with scissors! Computer wins!")
            computer_score += 1
        elif int(player_choice) == 2 and computer_choice == 1:
            print(f"\nYou chose {pchoice_as_string}...")
            print(f"Computer chose {cchoice_as_string}..")
            print("Cut my paper into pieces... Player wins!")
            player_score += 1

        print(f"\nPlayer: {player_score} Computer: {computer_score}")

        keep_playing = input("Keep playing? [y/n]?")
        if not keep_playing.lower() == "y":
            print("Coward!")
            break
else:
    sys.exit()
