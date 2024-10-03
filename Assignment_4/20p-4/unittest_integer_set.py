import unittest
import random
from random import randint

from integer_set import *
random.seed(0)

UPPER_LIMIT = integer_set.SETUPPERLIMIT
LOWER_LIMIT = 0
INVALID_SAMPLE_SIZE = 1000
VALID_SAMPLE_SIZE = 10
SAMPLE_MAX = 999999
VALID_SETS = (
    [1,2,3,4,5],
    [0,3,4,999,1000],
    [i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)],
    [randint(LOWER_LIMIT, UPPER_LIMIT + 1) for i in range(VALID_SAMPLE_SIZE)],
    [randint(LOWER_LIMIT, UPPER_LIMIT + 1)],
    []
)
INVALID_SETS = (
    [-1, 0, 1 , 2 ,3 ,4],
    [i for i in range(-1, UPPER_LIMIT + 2)]
)
INVALID_INTEGERS = ([random.randint(UPPER_LIMIT + 1, SAMPLE_MAX) for i in range(INVALID_SAMPLE_SIZE)] +
                    [random.randint(-SAMPLE_MAX, LOWER_LIMIT - 1) for i in range(INVALID_SAMPLE_SIZE)] +
                    [-1, UPPER_LIMIT + 1]
                    )
VALID_INTEGERS = [i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)]

class MyTestCase(unittest.TestCase):
    def test_can_init_with_data(self):
        for test_set in VALID_SETS:
            is_test = integer_set(test_set)
            self.assertEqual(test_set, is_test.get_elements())

    def test_can_insert_and_delete(self):
        for test_set in VALID_SETS:
            is_test = integer_set()
            for value in test_set:
                is_test.insertElement(value)
                self.assertIn(value, is_test.get_elements())
                is_test.deleteElement(value)
                self.assertNotIn(value, is_test.get_elements())

    def test_insert_and_delete_ignore_and_reject_errors(self):
        is_test = integer_set()
        for num in INVALID_INTEGERS:
            is_test.insertElement(num)
            self.assertNotIn(num, is_test.get_elements())
            is_test.deleteElement(num)

    def test_equals(self):
        for test_set in VALID_SETS:
            is_test1 = integer_set(test_set)
            self.assertTrue(is_test1.equals(is_test1))
            is_test2 = integer_set(test_set)
            self.assertTrue(is_test1.equals(is_test2))
            self.assertTrue(is_test2.equals(is_test1))
            # Delete a random index
            is_test2.deleteElement(test_set[randint(0,len(test_set) - 1)])
            self.assertFalse(is_test1.equals(is_test2))
            self.assertFalse(is_test2.equals(is_test1))

    def test_has_element(self):
        is_test = integer_set()
        for num in VALID_INTEGERS:
            is_test.insertElement(num)
            self.assertTrue(is_test.hasElement(num))
        for num in INVALID_INTEGERS:
            is_test.insertElement(num)
            self.assertFalse(is_test.hasElement(num))

if __name__ == '__main__':
    unittest.main()
