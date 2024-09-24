import unittest
import scramble

TESTS = (
    """"
    According to research at an English university, it does not matter in what order the letters in
    a word are, the only important thing is that the first and last letter are in the right place.
    The rest can be a total mess and you can still read it without a problem. This is because we 
    do not read every letter by itself but the word as a whole and the brain figures it out 
    anyway.
    """,
    "This is a sentence which contains contractions like can't, won't, shouldn't and isn't.",
    "This is a sentence with words that repeat: Words Words Words Words Words Words Words Words",
    "This is a sentence with, hy-phen-ation/dashes-",
    "",
    " ",
)

SAMPLE_COUNT = 10000
MARGIN_OF_ERROR = 0.05


class MyTestCase(unittest.TestCase):
    def test_manual(self):
        # TODO: Automate this test, ns how exactly as this program's output is rng dependent though
        for test in TESTS:
            print(f"Scrambling:\n{test}")
            print(f"Got:\n{scramble.scramble_words(test)}")

    def test_manual_no_regex(self):
        # TODO: Automate this test, ns how exactly as this program's output is rng dependent though
        for test in TESTS:
            print(f"Scrambling:\n{test}")
            print(f"Got:\n{scramble.scramble_words_no_regex(test)}")

    def test_shuffle_distribution (self):
        """
        Verify that shuffle() produces a uniform distribution
        """
        # Generate a sample list of numbers
        values = range(10)
        # Prepare a list of indices to count
        count = {i: 0 for i in values}
        for _ in range(SAMPLE_COUNT):
            shuffled_list = scramble.shuffle(values)
            # For each of the indices of the list add the value in the shuffled list to it's count
            for index, value in enumerate(values):
                count[value] += shuffled_list[index]
        # For a uniform distribution we'd assume the final count for each index should be roughly the same
        # (within some margin of error)
        print(count)
        mean_value = sum(count.values()) / len(count.values())
        print(f"{mean_value=}")
        # which we verify by confirming that each index is between the mean value plus or minus the margin
        for value in count.values():
            self.assertGreater(mean_value * (1 + MARGIN_OF_ERROR), value)
            self.assertLess(mean_value * (1 - MARGIN_OF_ERROR), value)


if __name__ == '__main__':
    unittest.main()
