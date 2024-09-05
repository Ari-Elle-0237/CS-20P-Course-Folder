#! /usr/bin/python3
"""
Assignment #2: Word Scrambler
loan.py
by Ariel Zepezauer
"""
import re
import random

def main():
    print(f"Aríel Zepezauer, arielzepezauer@gmail.com\n"
          f"Due: Thu Sep 9, 2024 7:00pm, "
          f"Assignment #2: Program Two (Word Scrambler)")
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
        # Skip words with length one as attempting to scramble them will add characters
        if len(word) == 1:
            continue
        # Save the beginning and end
        first, last = word[0], word[-1]
        # And then scramble the middle
        middle = word[1:-1]

        # TODO: Replace this with a fisher-yates shuffle (found in /PythonExamples/shuffle.py)
        # (Source: https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python)
        middle = ''.join(random.sample(middle, len(middle)))

        # Then save it for later
        substitutions.append((first + middle + last, word))
    # Then once all words are scrambled, replace the words in the original string with
    # their scrambled versions
    # TODO: Fix this replacing all duplicate words with their scrambled versions
    # (Perhaps re.sub is no the appropriate function for this,
    # and instead saving the locations of each word would be better.
    # research how re.Match objects work, and see if they capture this date)
    for substitution in substitutions:
        string = re.sub(substitution[1],substitution[0], string)
    return string

if __name__ == "__main__":
    main()