"""
Generates a "poor-man's" bar-chart of the number of letters for an input string.
"""
import argparse
from collections import defaultdict


def main():

    arg_parser = argparse.ArgumentParser(description="Will show you the number of letters in the string.")
    arg_parser.add_argument("-t", "--text",
                            help="String (text) we will count the characters for.")
    args = arg_parser.parse_args()

    if args.text:
        text = args.to_latin
    else:
        text = input("Please enter the string you would like to have counted:\n")
    bar_chart = defaultdict(list)

    for word in text.split():
        word = word.lower()
        for char in word:
            bar_chart[char].append(char)

    for key in bar_chart.keys():
        print(f"{bar_chart[key]} : {len(bar_chart[key])}")


if __name__ == "__main__":
    main()
