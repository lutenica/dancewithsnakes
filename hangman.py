#!/usr/bin/python3
"""
    A simple take on hangman
"""
import random
from english_words import english_words_set

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(list(english_words_set))


game_over = False

lives = 6

display = []

print("Welcome to hangman!")

for letter in chosen_word:
    display += '_'

while not game_over:

    if '_' not in display:

        game_over = True
        print("You win!")

    print(f"{' '.join(display)}")

    guessed = False

    guess = input("Guess a letter:\n").lower()

    for position in range(len(chosen_word)):

        letter = chosen_word[position]

        if guess == letter:

            if guess in display:

                print(f"You've guessed {guess}")

            display[position] = letter
            guessed = True

    if not guessed:

        lives -= 1
        print(stages[lives])

    if lives == 0:

        print("You loose!")
        print(f"The word was:{chosen_word}")
        game_over = True
