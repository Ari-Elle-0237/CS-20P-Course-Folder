# shuffle.py
# Steve J. Hodges, Cabrillo College, sthodges@cabrillo.edu
# demonstration of a standard random shuffle of a list

import sys
import random

# findMax
# Fisher-Yates shuffle of a list
def shuffle(values) :
   swaptarget = 0
   size = len(values)
   for i in range(size-1, 0, -1):
      swaptarget = random.randint(0, i)
      values[i], values[swaptarget] = values[swaptarget], values[i] # standard swap


# "main"
myValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("before:")
print(myValues)
shuffle(myValues)
print("After shuffle:")
print(myValues)