#! /usr/bin/python3
"""
Assignment #2: Word Scrambler
scramble.py
by Ariel Zepezauer (arielzepezauer@gmail.com
Pengo: 'azepezau'
Test Cases in scramble_unittest.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
"""

import re
import random


def main():
    print(f"Aríel Zepezauer, arielzepezauer@gmail.com\n"
          f"Due: Thu Sep 9, 2024 7:00pm, "
          f"Assignment #2: Program Two (Word Scrambler)\n"
          f"Exit Code 0: passes most test cases but still has bugs")
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
        # <editor-fold>
        # Alternate phrasing for the if statement below with less indentation but uses 'continue'
        # (Personally I find this cleaner but style guide for the class prohibits this)
        # if len(word) == 1:
        #     continue
        # </editor-fold>
        # Skip words with length one as attempting to scramble them will add characters
        if len(word) != 1:
            # Save the beginning and end
            first, last = word[0], word[-1]
            # And then scramble the middle
            middle = word[1:-1]
            middle = shuffle(middle)
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
    # TODO: Replace this line with a fisher-yates shuffle (found in /PythonExamples/shuffle.py)
    # (Source: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python)
    return ''.join(random.sample(iterable, len(iterable)))

if __name__ == "__main__":
    main()