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

def scramble_string(string):
    words = re.findall(r"\W?[A-Za-z]*\W?", string)
    substitutions = []
    for word in words:
        first, last = word[0], word[-1]
        middle = word[1:-2]
        middle = middle.scramble()
        substitutions.append((first + middle + last, word))
    for substitution in substitutions:
        re.sub(substitution[0],substitution[1], string)
    return string

if __name__ == "__main__":
    main()