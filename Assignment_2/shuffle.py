# shuffle.py
# Steve J. Hodges, Cabrillo College, sthodges@cabrillo.edu
# demonstration of a standard random shuffle of a list

import sys
import random


# findMax
# Fisher-Yates shuffle of a list
def shuffle(values):
    swaptarget = 0
    size = len(values)
    for i in range(size - 1, 0, -1):
        swaptarget = random.randint(0, i)
        values[i], values[swaptarget] = values[swaptarget], values[i]  # standard swap


def shuffle2(iterable):
    shuffle_index = 0
    for i in iterable:
        target_index = random.randint(shuffle_index, len(iterable) - 1)
        iterable[shuffle_index], iterable[target_index] = iterable[target_index], iterable[shuffle_index]
        shuffle_index += 1
    return iterable
    # "main"


myValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("before:")
print(myValues)
myValues = shuffle2(myValues)
print("After shuffle:")
print(myValues)
print(str("".join(["a","b","c"])))