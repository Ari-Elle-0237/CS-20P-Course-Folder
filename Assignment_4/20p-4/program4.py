# a "main function" containing a test routine
# this is not an exhaustive test routine so
# please do conduct your own testing in addition!
# this code goes in your program4.py file:
import integer_set
import random
import unittest_integer_set

random.seed(0)

is1 = integer_set.integer_set()
is2 = integer_set.integer_set([1, 2, 5])
is3 = integer_set.integer_set([4])

print("CS20p Integer Sets")
print("<put your name and email here>")

is1.insertElement(2);
is1.insertElement(4)
is1.insertElement(2);
is1.insertElement(3)
is1.insertElement(5);
is1.insertElement(7)
is1.deleteElement(3);
is1.deleteElement(7)
is1.deleteElement(9)

for i in range(0, int(is3.getUpperLimit() * 0.10)):
    is3.insertElement(random.randint(0, is3.getUpperLimit()))
print("is3 (random):");
print(is3);
is3.unionOf(is1, is2);
print("is3 (union):");
print(is3);
is3.intersectionOf(is1, is2);
print("is3 (intersection):");
print(is3);
if (is3.equals(is3)):
    print("1: is3 == is3")
else:
    print("1: is3 != is3")
if (is3.equals(is2)):
    print("2: is3 == is2")
else:
    print("2: is3 != is2")
if (is1.hasElement(5)):
    print("3: is1 has 5")
else:
    print("3: is1 does not have 5")
if (is1.hasElement(7)):
    print("4: is1 has 7")
else:
    print("4: is1 does not have 7")

test_case = unittest_integer_set.MyTestCase()
unittest_integer_set.unittest.main(test_case)