#! /usr/bin/python3
"""
Assignment #3: Pattern Matching
pattern.py
by Ariel Zepezauer (arielzepezauer@gmail.com)
Pengo: 'azepezau'
Test Cases in unittest_pattern.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: Thu Oct 3, 2024 7:00pm
Python Version 3.12
Exit Code 0: Passes all current tests
"""
import sys

PATTERNS = [int(i, base=2) for i in """
00000000000000000000000000000000
01010101010101010101010101010101
00110011001100110011001100110011
01100110011001100110011001100110
00001111000011110000111100001111
01011010010110100101101001011010
00111100001111000011110000111100
01101001011010010110100101101001
00000000111111110000000011111111
01010101101010100101010110101010
00110011110011000011001111001100
01100110100110010110011010011001
00001111111100000000111111110000
01011010101001010101101010100101
00111100110000110011110011000011
01101001100101100110100110010110
00000000000000001111111111111111
01010101010101011010101010101010
00110011001100111100110011001100
01100110011001101001100110011001
00001111000011111111000011110000
01011010010110101010010110100101
00111100001111001100001111000011
01101001011110011001011010010110
00000000111111111111111100000000
01010101101010101010101001010101
00110011110011001100110000110011
01100110100110011001100101100110
00001111111100001111000000001111
01011010101001011010010101011010
00111100110000111100001100111100
01101001100101101001011001101001
""".strip().split("\n")]


def main():
    for line in sys.stdin:
        if line == "":
            pass
        elif match_patterns(line) == -1:
            print("error")
        else:
            print(match_patterns(line))


def match_patterns(num):
    """
    Takes a given number and compares it to all the patterns in PATTERNS, returning the index of the closest
    matching pattern or -1 if none match.
    :param num: The number to be compared against PATTERNS
    :return: -1 or an int between 0 and 7 (inclusive)
    """
    return min(                                 # The closest match can be found by taking the minimum of our patterns:
        [(i, v) for i, v in enumerate(PATTERNS) # First make a list comprehension of our patterns and their indices
        if compare_bits(v, num) <= 7],          # But only include the patterns that aren't too different
        key=lambda x: compare_bits(x[1], num),  # Then calculate the minimum based on v's differences to num
        default=                                # But set a default of -1 if the list comprehension is empty *
        (-1, None)                              # (*: this is in a tuple so it works with the next line)
        )[0]                                    # Finally return the index of our minimum pattern (or -1)
    # In condensed form:
    # return min([(i, v) for i, v in enumerate(PATTERNS) if compare_bits(v, num) <= 7],
    #            key=lambda x: compare_bits(x[1], num), default=(-1, None))[0]

def compare_bits(bits_a, bits_b):
    # XOR A and B together, then count the number of ones in the resulting binary number to get the differences
    return (bits_a ^ bits_b).bit_count()


if __name__ == "__main__":
    main()
