"""
Simple anagram finder.
"""
from collections import Counter
import argparse
import requests

words_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"


def main():
    arg_parser = argparse.ArgumentParser(description="Finds anagrams for the provided word based on dict files")
    arg_parser.add_argument("-w", "--word",
                            help="Word to find anagrams for.")
    args = arg_parser.parse_args()

    if args.word:
        user_word = args.word
    else:
        user_word = input("Word you would like to find anagrams for:\n")

    word_list = get_words(words_url)
    anagrams = find_anagrams(user_word, word_list)
    print(f"There are {len(anagrams)} anagrams for {user_word}:")
    print(f"{' '.join(anagrams)}")


def get_words(url):
    """
    Returns a list of the words that match
    :param url:
    :return: list of strings
    """
    r = requests.get(url=url)
    r.raise_for_status()
    return r.text.splitlines()


def find_anagrams(user_word, word_list):
    """
    Finds anagrams of the given string in the list of strings
    :param user_word: The string to search for
    :param word_list: The list to search in
    :return: List of anagrams
    """
    target_length = len(user_word)
    user_counter = Counter(user_word)
    anagrams = []

    for word in word_list:
        if len(word) == target_length:
            word_counter = Counter(word)
            if word_counter == user_counter:
                anagrams.append(word)

    anagrams.remove(user_word)
    return anagrams


if __name__ == "__main__":
    main()
