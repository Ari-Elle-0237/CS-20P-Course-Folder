import unittest
from pattern import *

# TODO: Learn how to write unittests that use stdin/out and can actually test main()

SAMPLE_RUNS = [
    (0b01100110100110010110011010011001, 11,),
    (0b00110011010011000011001111001100, 10,),
    (0b00110010001100110011001100110001, 2,),
    (0b00000010000010010000001100000000, 0,),
    (0b11110110100101111010010101110101, -1,),
    (0b01011000110101010101101001001010, 5),
]


class MyTestCase(unittest.TestCase):
    def test_patterns_match_self(self):
        for i, pattern in enumerate(PATTERNS):
            self.assertEqual(i, match_patterns(pattern),)
    def test_sample_runs(self):
        for run in SAMPLE_RUNS:
            self.assertEqual(run[1], match_patterns(run[0]))

if __name__ == '__main__':
    unittest.main()
