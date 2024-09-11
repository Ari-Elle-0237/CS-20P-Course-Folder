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
    # Regex to compile a list of all re.Match objects for all words in the string,
    # (Explanation: Words must begin with at least one word character,
    # then any  internal punctuation may also match as long as it's followed by another word character)
    words = re.finditer(r"[\w]+(?:[-']+[\w]+)*", string)
    for match in words:
        # Get the string from the re.Match object (ns if it's better style to use match.group() or match[0] here)
        word = match.group()
        # Only proceed if the string is longer than 1 to avoid problems.
        # <editor-fold: Alternate phrasing>
        # Alternate phrasing for the if statement below with less indentation but use of 'continue'
        # (Personally I find this cleaner but style guide for the class prohibits this)
        # if len(word) == 1:
        #     continue
        # </editor-fold>
        if len(word) > 1:
            # Save the beginning and end
            first, last = word[0], word[-1]
            # Scramble the middle
            middle = word[1:-1]
            middle = shuffle_string(middle)
            # Then update the string
            string = string[:match.start()] + first + middle + last + string[match.end():]
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


def shuffle_string(string):
    return "".join(shuffle(string))
    # <editor-fold: Alternate Phrasing>
    # # Alternate 1 line phrasing for personal future reference
    # # (Source: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python)
    # return ''.join(random.sample(string, len(string)))
    # </editor-fold>


if __name__ == "__main__":
    main()