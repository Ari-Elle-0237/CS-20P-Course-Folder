import unittest
import loan

class TestCase(unittest.TestCase):
    def test_formula(self):
        payment = loan.calculate_payment(10000, 0.12, 4, 12)
        self.assertEqual(263.34, round(payment, 2))

    def test_input(self):
        pass

if __name__ == '__main__':
    unittest.main()
