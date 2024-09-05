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
    ui = input("Scramble A String:")
    print(scramble_word(ui))

def scramble_word(string):
    words = re.findall(r"[\w']+", string)
    substitutions = []
    for word in words:
        if len(word) == 1:
            continue
        first, last = word[0], word[-1]
        middle = word[1:-1]

        # This line is from:
        # https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python
        middle = ''.join(random.sample(middle, len(middle)))

        substitutions.append((first + middle + last, word))
    print(substitutions)
    for substitution in substitutions:
        string = re.sub(substitution[1],substitution[0], string)
    return string

if __name__ == "__main__":
    main()