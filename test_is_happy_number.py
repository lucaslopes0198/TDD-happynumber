import unittest
from is_happy_number import isHappyNumber

class testIsHappyNumber(unittest.TestCase):

    def test_is_happy_number(self):
        num = isHappyNumber()
        result = num.is_happy_number(7)
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
