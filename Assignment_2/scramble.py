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
"""

import re
import random
import sys


def main():
    for line in sys.stdin:
        print(scramble_words(line))

def scramble_words(string):
    """
    Scrambles the individual words in a string, while preserving the first and last letters.
    ie: "These are word's" -> "Teshe are wrd'os"
    :param string: to be scrambled
    :return: scrambled string
    """
    # Regex to compile a list of all re.Match objects for all words in the string,
    words = re.finditer(r"\w+", string)
    # <editor-fold: Alternate Pattern>
    # alternate pattern which allows apostrophes and hyphens: r"[\w]+(?:[-']+[\w]+)*"
    # (Pattern Explanation: Words must begin with at least one word character, then any internal punctuation may also
    # match as long as it's followed by another word character)
    # </editor-fold>
    for match in words:
        # Get the string from the re.Match object
        word = match.group()  # (ns if it's better style to use match.group() or match[0] here)
        # Then, only proceed if the string is long enough to be scrambled to avoid problems
        # <editor-fold: Alternate phrasing>
        # Alternate phrasing for the if statement below with less indentation but use of 'continue'
        # (Personally I find this cleaner but style guide for the class prohibits this)
        # if len(word) == 1:
        #     continue
        # </editor-fold>
        if len(word) > 3:
            unshuffled_word = word
            # Enter a while loop to ensure that the shuffle hasn't reproduced the original by chance
            while word == unshuffled_word:
                word = word[0] + shuffle_string(word[1:-1]) + word[-1]
            # Then update the string
            string = string[:match.start()] + word + string[match.end():]
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