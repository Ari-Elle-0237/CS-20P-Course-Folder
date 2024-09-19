import unittest
from pattern import *

class MyTestCase(unittest.TestCase):
    def test_patterns_match_self(self):
        for i, pattern in enumerate(PATTERNS):
            self.assertEqual(i, match_patterns(pattern),)



if __name__ == '__main__':
    unittest.main()
