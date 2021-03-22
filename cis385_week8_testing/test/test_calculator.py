import unittest
from app.main import calculator


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(2, 1), 3)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)
        self.assertNotEqual(calculator.divide(10, 5), 3)
        self.assertEqual(calculator.divide(-10, 5), -2)
        self.assertEqual(calculator.divide(-10, -5), 2)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()