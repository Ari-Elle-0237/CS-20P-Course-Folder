#! /usr/bin/python3
"""
Assignment #2: (Program 2) Word Scrambler
scramble.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in unittest_scramble.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: Thu Sep 19, 2024 7:00pm
Exit Code 0: Passes current test cases and visual inspection

Edit notes: updated regex to no longer handle internal punctuation, (my apologies for doing so, I was just trying to
think of edge cases that still met the assignment requirements in order to challenge myself)
"""

import re
import random
import sys


def main():
    for line in sys.stdin:
        # print(scramble_words(line))
        print(scramble_words_no_regex(line))

def scramble_words(string):
    """
    Scrambles the individual words in a string, while preserving the first and last letters.
    ie: "These are word's" -> "Teshe are wrd'os"
    :param string: to be scrambled
    :return: scrambled string
    """
    words = re.finditer(r"\w+", string)  # compile a list of re.Match objects for all words in the string,
    # <editor-fold: Alternate Pattern>
    # alternate pattern which allows apostrophes and hyphens: r"[\w]+(?:[-']+[\w]+)*"
    # (Pattern Explanation: Words must begin with at least one word character, then any internal punctuation may also
    # match as long as it's followed by another word character)
    # </editor-fold>
    for match in words:
        word = match.group()  # Get the string from the re.Match object
        if len(word) > 3:  # Only proceed if the string is long enough to be scrambled to avoid problems
            # <editor-fold: Alternate phrasing>
        # Alternate phrasing for the if statement below with less indentation but use of 'continue'
        # (Personally I find this cleaner but style guide for the class prohibits this)
        # if len(word) == 1:
        #     continue
        # </editor-fold>
            unshuffled_word = word
            while word == unshuffled_word: # Enter a while loop to correct shuffle reproducing the original by chance
                word = word[0] + shuffle_string(word[1:-1]) + word[-1]
            string = string[:match.start()] + word + string[match.end():]  # Then update the string
    return string

def scramble_words_no_regex(string):
    """
    Alternate scramble words which does not use regex, at the cost of not preserving whitespace or handling \n, \t, etc.
    (I will note avoiding regex was not a listed requirement of the assignment or against style guidelines...)
    :param string: to be scrambled
    :return: scrambled string
    """
    words = string.split(" ")
    ret_string = ""
    for word in words:
        if len(word) > 3:  # Only proceed if the string is long enough to be scrambled to avoid IndexError problems
            unshuffled_word = word
            while word == unshuffled_word:  # Enter a while loop to ensure that the shuffle hasn't reproduced the original by chance
                if word[-1].is_alphanum(): # Ignore the last character if it's non-alphanumeric
                    word = word[0] + shuffle_string(word[1:-1]) + word[-1]
                else:
                    word = word[0] + shuffle_string(word[1:-2]) + word[-2]
            ret_string += word + " "  # Then update the string
    return string


def shuffle(iterable):
    """
    Shuffles an iterable using the Fisher-Yates algorithm described in class
    :param iterable: to be shuffled
    :return: scrambled list of values in the shuffled iterable
    """
    shuffle_index = 0
    iterable = list(iterable)
    for _ in iterable:
        target_index = random.randint(shuffle_index, len(iterable) - 1)
        iterable[shuffle_index], iterable[target_index] = iterable[target_index], iterable[shuffle_index]
        shuffle_index += 1
    return iterable


# Extends shuffle() to make it return a string instead of a list
def shuffle_string(string):
    return "".join(shuffle(string))
    # <editor-fold: Alternate Phrasing>
    # # Alternate 1 line phrasing for personal future reference
    # # (Source: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python)
    # return ''.join(random.sample(string, len(string)))
    # </editor-fold>


if __name__ == "__main__":
    main()