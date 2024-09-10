import unittest
import scramble

tests = (
    """"
    According to research at an English university, it does not matter in what order the letters in
    a word are, the only important thing is that the first and last letter are in the right place.
    The rest can be a total mess and you can still read it without a problem. This is because we 
    do not read every letter by itself but the word as a whole and the brain figures it out 
    anyway.
    """,
    """
    This is a sentence which contains contractions like can't, won't, shouldn't and isn't.
    """,
    """
    This is a sentence with words that repeat: Words Words Words Words Words Words Words
    """
         )



class MyTestCase(unittest.TestCase):
    def test_manual(self):
        for test in tests:
            print(f"Scrambling:\n{test}")
            print(f"Got:\n{scramble.scramble_words(test)}")


if __name__ == '__main__':
    unittest.main()
