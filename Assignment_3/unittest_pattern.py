import sys
import unittest
from pattern import *
import pattern

SAMPLE_RUNS = [
    ("01100110100110010110011010011001", 11,),
    ("00110011010011000011001111001100", 10,),
    ("00110010001100110011001100110001", 2,),
    ("00000010000010010000001100000000", 0,),
    ("11110110100101111010010101110101", -1,),
    ("01011000110101010101101001001010", 5),
]

import subprocess
class MyTestCase(unittest.TestCase):
    def test_patterns_match_self(self):
        print("begin:")
        for i, v in enumerate(PATTERNS):
            pattern.main([bin(v)])
            with open(sys.stdout) as o:
                print(o.read)
            print([out, i])
            print(type(out))
            # self.assertEqual(i, out)

    def test_sample_runs(self):
        for run in SAMPLE_RUNS:
            self.assertEqual(run[1], match_patterns(run[0]))

if __name__ == '__main__':
    unittest.main()
