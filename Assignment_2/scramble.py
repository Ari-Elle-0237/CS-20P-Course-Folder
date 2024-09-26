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

Patch Notes/Explanations vs. Previous submission:
- Made repository private: might come to office hours for help setting up keys so I can access it from the command
line again if I can't figure it out on my own, as using my GH password appears to be insufficient. For now I have just
been unprivating to make a git pull and then reprivating if that's ok.

- added scramble_words_no_regex() to comply with feedback. (For the record, I am aware regex is overkill for this
assignment, I only used it because I had already been wanting to teach myself more about python's regex library
(I am also already pretty comfortable reading and writing regex from my own prior experience) thus I felt it was an
appropriate solution since in a way, it was sort of my goal to have "two problems" lol.)

- updated regex to no longer handle internal punctuation

- removed read_stdin()

- Abridged some comments for better readability

- Simplified the "Shuffle the word" step per feedback

- Assuming I read you correctly, I could not replicate the issue with the program hanging on blank line, empty file or
empty string tests regardless of whether I ran it through powershell or unittest or on the new attempt or the old one,
if the issue is still persisting with my amended version I can come to office hours to show you/ask what you meant in
your feedback.
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
    # Alternate pattern which allows apostrophes and hyphens: r"[\w]+(?:[-']+[\w]+)*"
    # Pattern Explanation: Words must begin with at least one word character, then any internal punctuation may also
    # match as long as it's followed by another word character, additional internal punctuation marks may be added by
    # placing them inside the set of brackets after '?:'
    # </editor-fold>
    for match in words:
        word = match.group()  # Get the string from the re.Match object
        if len(word) > 3:  # Only proceed if the string is long enough to be scrambled to avoid problems
            unshuffled_word = word
            while word == unshuffled_word: # Enter a while loop to correct shuffle reproducing the original by chance
                word = word[0] + shuffle_string(word[1:-1]) + word[-1] # Shuffle the word
            string = string[:match.start()] + word + string[match.end():]  # Then update the string with that word
    return string

def scramble_words_no_regex(string):
    """
    Alternate scramble_words() with no regex, at the cost of not preserving whitespace or handling \n, \t, etc. or
    leading punctuation properly.
    :param string: to be scrambled
    :return: scrambled string
    """
    words = string.split(" ")
    ret_string = ""  # Return String
    for word in words:
        if len(word) > 3:  # Only proceed if the string is long enough to be scrambled to avoid problems
            unshuffled_word = word
            while word == unshuffled_word:  # Enter a while loop to stop shuffle reproducing the original by chance
                if word[-1].isalnum(): # Ignore the last character if it's non-alphanumeric
                    word = word[0] + shuffle_string(word[1:-1]) + word[-1]
                else:
                    word = word[0] + shuffle_string(word[1:-2]) + word[-2]
            ret_string += word + " "  # Then update the string
    return ret_string


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