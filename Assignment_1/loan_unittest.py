import unittest
import loan

class TestCase(unittest.TestCase):
    def test_formula(self):
        # Format
        # ((Principal, Interest, Annual Payments, Years), Expected Answer)
        tests = (
            ((10000, 0.12, 12, 4), 263.34),
            ((680000, 0.0575, 12, 30), 3968.30),
            ((275000000, 0.005, 4, 5), 13931182.65),
            ((17000, 2.01, 52, 1), 763.34),
        )
        for test in tests:
            print(f"Testing Args:{test[0]}, expecting answer {test[1]}")
            payment = loan.calculate_payment(*test[0])
            print(f"Got {payment:0.2f}")
            self.assertEqual(test[1], round(payment, 2))

    def test_input(self):
        pass

if __name__ == '__main__':
    unittest.main()
