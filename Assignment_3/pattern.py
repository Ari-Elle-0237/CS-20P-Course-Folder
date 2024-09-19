#! /usr/bin/python3
"""
Assignment #3: Pattern Matching
pattern.py
by Ariel Zepezauer (arielzepezauer@gmail.com)
Pengo: 'azepezau'
Test Cases in unittest_pattern.py
Repository at: https://github.com/Ari-Elle-0237/CS-20P-Course-Folder.git
Due: Thu Oct 3, 2024 7:00pm
Python Version 3.10
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
    data = [int(i, base=2) for i in read_stdin().strip().split("\n")]
    for num in data:
        print(match_patterns(num))


def match_patterns(num):
    matches = []
    for i, pattern in enumerate(PATTERNS):
        bit_count = compare_bits(num, pattern)
        matches.append((i, bit_count))
    # source: https://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column
    matches.sort(key=lambda x: x[1], reverse=True)
    if matches[0][1] == -1:
        return -1
    return matches[0][0]


def compare_bits(bits_a, bits_b):
    # XOR A and B together, then count the number of ones in the resulting binary number to determine
    # the number of differences between, (Note: bit_count() is python 3.10+ only)
    bit_count = (bits_a ^ bits_b).bit_count()
    if bit_count <= 7:
        return bit_count
    return -1


def read_stdin():
    data = ''
    for line in sys.stdin:
        if line.strip() == "EOF":
            return data
        data += line
    return data


if __name__ == "__main__":
    main()
