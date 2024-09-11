#! /usr/bin/python3
"""
Assignment #2: (Program 2) Word Scrambler
scramble.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in scramble_unittest.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due:
Exit Code 0: passes current test cases but may still contain bugs, also shuffle() needs to be implemented
"""

import re
import random


def main():

    # TODO make this accept EOF and explicitly use stdin (see example in /PythonExample/findMax.py/)
    ui = input("Scramble A String:")
    print(scramble_words(ui))


def scramble_words(string):
    """
    Scrambles the individual words in a string, while preserving the first and last letters.
    ie: "These are word's" -> "Teshe are wrd'os"
    :param string: to be scrambled
    :return: scrambled string
    """
    # Regex to compile a list of all words in the string, apostrophes are also included to allow for contractions
    # (May be better to use \b\B in the expression instead, test and refactor later)
    words = re.findall(r"[\w']+", string)
    substitutions = []
    for word in words:
        # <editor-fold: Alternate phrasing>
        # Alternate phrasing for the if statement below with less indentation but uses 'continue'
        # (Personally I find this cleaner but style guide for the class prohibits this)
        # if len(word) == 1:
        #     continue
        # </editor-fold>
        # Skip words with length one as attempting to scramble them will cause problems
        if len(word) != 1:
            # Save the beginning and end
            first, last = word[0], word[-1]
            # And then scramble the middle
            middle = word[1:-1]
            middle = shuffle_string(middle)
            # Then save it for later
            substitutions.append((word, first + middle + last))
    # Then once all words are scrambled,
    # Replace the words in the original string with their scrambled versions
    # (re.sub is probably not the appropriate function for this,
    # should refactor this to use Match.pos and Match.endpos later)
    for substitution in substitutions:
        string = re.sub(*substitution, string, count=1)
    return string

def shuffle(iterable):
    """
    Shuffles an iterable using the fisher-yates algorithm described in class
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
    # <editor-fold: Alternate Phrasing>
    # # Alternate 1 line phrasing for personal future reference
    # # (Source: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python)
    # return ''.join(random.sample(iterable, len(iterable)))
    # </editor-fold>


def shuffle_string(string):
    return "".join(shuffle(string))


if __name__ == "__main__":
    main()