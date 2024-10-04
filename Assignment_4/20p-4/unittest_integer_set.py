import unittest
import random
from random import randint

from integer_set import integer_set
random.seed(0)

# <editor-fold: CONSTANTS>
UPPER_LIMIT = integer_set.SETUPPERLIMIT
LOWER_LIMIT = 0
INVALID_SAMPLE_SIZE = 100
VALID_SAMPLE_SIZE = 10
SAMPLE_MAX = 9999
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
INVALID_INTEGERS = [random.randint(UPPER_LIMIT + 1, SAMPLE_MAX) for i in range(INVALID_SAMPLE_SIZE)] +\
                   [random.randint(-SAMPLE_MAX, LOWER_LIMIT - 1) for i in range(INVALID_SAMPLE_SIZE)] +\
                   [-1, UPPER_LIMIT + 1]
VALID_INTEGERS = [i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)]
# Format: ([set1], [set2], [intersection of set1 and set2]
INTERSECTION_TESTS = (
    ([0,1,2,3],[2,3,4],[2,3]),
    ([1000], [2, 3, 4], []),
    ([999, 1000], [2, 3, 999, 1000], [999,1000]),
    ([0,2,3], [0,4,5,6,2], [0,2]),
    ([-1], [2, 3, 4], []),
    ([],[],[]),
    ([LOWER_LIMIT], [LOWER_LIMIT], [LOWER_LIMIT]),
    ([UPPER_LIMIT], [UPPER_LIMIT], [UPPER_LIMIT]),
    ([randint(LOWER_LIMIT, UPPER_LIMIT + 1)],[],[]),
    ([randint(LOWER_LIMIT, UPPER_LIMIT + 1)], [-1], []),
    ([i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)],[1001],[]),
    ([i for i in range(LOWER_LIMIT, UPPER_LIMIT + 1)], [1000], [1000]),
)
INTERSECTION_TESTS_BYTES_COMPATIBLE = (
    ([0,1,2,3],[2,3,4],[2,3]),
    ([1000], [2, 3, 4], []),
    ([999, 1000], [2, 3, 999, 1000], [999,1000]),
    ([0,2,3], [0,4,5,6,2], [0,2]),
    ([-1], [2, 3, 4], []),
    ([],[],[]),
    ([LOWER_LIMIT], [LOWER_LIMIT], [LOWER_LIMIT]),
    ([UPPER_LIMIT], [UPPER_LIMIT], [UPPER_LIMIT]),
    ([randint(LOWER_LIMIT, UPPER_LIMIT + 1)],[],[]),
    ([randint(LOWER_LIMIT, UPPER_LIMIT + 1)], [-1], []),
    ([i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)],[1001],[]),
    ([i for i in range(LOWER_LIMIT, UPPER_LIMIT + 1)], [1000], [1000]),
)

# Format: ([set1], [set2], [union of set1 and set2]
UNION_TESTS = (
    ([0,1,2,3],[2,3,4],[0,1,2,3,4]),
    ([1000], [2, 3, 4], [2,3,4,1000]),
    ([-1], [2, 3, 4], [2,3,4]),
    ([], [], []),
    ([UPPER_LIMIT], [UPPER_LIMIT], [UPPER_LIMIT]),
    ([LOWER_LIMIT], [LOWER_LIMIT], [LOWER_LIMIT]),
    ([i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)],[1001],[i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)]),
    ([i for i in range(LOWER_LIMIT, UPPER_LIMIT + 1)], [randint(LOWER_LIMIT, UPPER_LIMIT + 1)],
     [i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)]),
)
UNION_TESTS_BYTES_COMPATIBLE = (
    ([0,1,2,3],[2,3,4],[0,1,2,3,4]),
    ([1000], [2, 3, 4], [2,3,4,1000]),
    ([-1], [2, 3, 4], [2,3,4]),
    ([], [], []),
    ([UPPER_LIMIT], [UPPER_LIMIT], [UPPER_LIMIT]),
    ([LOWER_LIMIT], [LOWER_LIMIT], [LOWER_LIMIT]),
    ([i for i in range(LOWER_LIMIT, UPPER_LIMIT + 1)], [randint(LOWER_LIMIT, UPPER_LIMIT + 1)],
     [i for i in range(LOWER_LIMIT,UPPER_LIMIT + 1)]),
)

# </editor-fold>

class TestIntegerSet(unittest.TestCase):
    def test_can_init_with_data(self):
        for test_set in VALID_SETS:
            is_test = integer_set(test_set)
            self.assertEqual(sorted(test_set), is_test.get_elements())

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
            try:
                is_test2.deleteElement(test_set[randint(0,len(test_set) - 1)])
                self.assertFalse(is_test1.equals(is_test2))
                self.assertFalse(is_test2.equals(is_test1))
            except ValueError: # pass ValueError for issues with empty range in the randint function
                pass

    def test_has_element(self):
        is_test = integer_set()
        for num in VALID_INTEGERS:
            is_test.insertElement(num)
            self.assertTrue(is_test.hasElement(num))
        for num in INVALID_INTEGERS:
            self.assertFalse(is_test.hasElement(num))
            is_test.insertElement(num)
            self.assertFalse(is_test.hasElement(num))

    def test_intersection(self):
        for test_case in INTERSECTION_TESTS:
            set1,set2,expected = test_case
            is_test1 = integer_set(set1)
            is_test2 = integer_set(set2)
            is_test3 = integer_set(VALID_SETS[randint(0,len(VALID_SETS) - 1)])
            is_test3.intersectionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())
            is_test2.intersectionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())

    def test_union(self):
        for test_case in UNION_TESTS:
            set1,set2,expected = test_case
            is_test1 = integer_set(set1)
            is_test2 = integer_set(set2)
            is_test3 = integer_set(VALID_SETS[randint(0,len(VALID_SETS) - 1)])
            is_test3.unionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())
            is_test2.unionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())

# (Uncomment below to toggle shadowing (necessary for TestPositiveIntegerSetBytes to pass)
# from integer_set import PositiveIntegerSetBytes as integer_set
# This does not seem like the right way to do this, but ns what the right way is
from integer_set import PositiveIntegerSetBytes
class TestPositiveIntegerSetBytes(TestIntegerSet):
    def test_intentional_shadowing(self):
        self.assertIsInstance(integer_set(), PositiveIntegerSetBytes)

    def test_can_init_with_data(self):
        super().test_can_init_with_data()

    def test_can_insert_and_delete(self):
        super().test_can_insert_and_delete()

    def test_can_insert_and_delete_beyond_1k(self):
        is_test = integer_set()
        for num in [abs(i) for i in INVALID_INTEGERS]:
            is_test.insertElement(num)
            self.assertIn(num, is_test.get_elements())
            is_test.deleteElement(num)

    def test_insert_and_delete_ignore_and_reject_errors(self):
        is_test = integer_set()
        for num in [-abs(i) for i in INVALID_INTEGERS]:
            is_test.insertElement(num)
            self.assertNotIn(num, is_test.get_elements())
            is_test.deleteElement(num)


    def test_equals(self):
        super().test_equals()

    def test_has_element(self):
        is_test = integer_set()
        for num in VALID_INTEGERS + [abs(i) for i in INVALID_INTEGERS]:
            is_test.insertElement(num)
            self.assertTrue(is_test.hasElement(num))
        for num in [-abs(i) for i in INVALID_INTEGERS]:
            self.assertFalse(is_test.hasElement(num))
            is_test.insertElement(num)
            self.assertFalse(is_test.hasElement(num))

    def test_intersection(self):
        for test_case in INTERSECTION_TESTS_BYTES_COMPATIBLE:
            set1,set2,expected = test_case
            is_test1 = integer_set(set1)
            is_test2 = integer_set(set2)
            is_test3 = integer_set(VALID_SETS[randint(0,len(VALID_SETS) - 1)])
            is_test3.intersectionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())
            is_test2.intersectionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())

    def test_union(self):
        for test_case in UNION_TESTS_BYTES_COMPATIBLE:
            set1,set2,expected = test_case
            is_test1 = integer_set(set1)
            is_test2 = integer_set(set2)
            is_test3 = integer_set(VALID_SETS[randint(0,len(VALID_SETS) - 1)])
            is_test3.unionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())
            is_test2.unionOf(is_test1,is_test2)
            self.assertEqual(expected,is_test3.get_elements())

# (Uncomment below to toggle shadowing (necessary for TestIntegerSetBytes to pass)
from integer_set import IntegerSetBytes
# This does not seem like the right way to do this, but ns what the right way is
class TestIntegerSetBytes(TestPositiveIntegerSetBytes):
    pass

if __name__ == '__main__':
    unittest.main()
