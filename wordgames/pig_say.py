"""
    The almighty talking pig! It shall speak Latin for you! Though it just speaks back at you, so
    it's more like a parrot really...
"""
import argparse


def pig_say():
    """
        Handles the user input
    """
    arg_parser = argparse.ArgumentParser(description="Behold, the almighty pig. It speaks latin!")
    arg_parser.add_argument("-t", "--to_latin",
                            help="String to translate to pig latin. Use quotes for sentences.")
    args = arg_parser.parse_args()

    if args.to_latin:
        translate = args.to_latin
    if not translate:
        translate = input("Please enter the phrase/word you would like to translate:\n")

    latin(translate)


def latin(string):
    """

    Does translation to "latin"

    :param string:
        The string we want to translate
    """
    consonants = set("bcdfghjklmnpqrstvwxyz")
    words = string.split()
    new_words = []
    # Translate to latin
    for word in words:

        new_word = None

        if word[0].lower() in consonants:
            remove = word[0]
            # Two syllable consonants:
            if word[1].lower() in consonants:
                remove += word[1]

            new_word = word.removeprefix(remove).capitalize() + remove.lower() + "ay"

        else:

            new_word = word.capitalize() + "yay"

        new_words.append(new_word)

    print(" ".join(new_words))


if __name__ == "__main__":
    pig_say()
