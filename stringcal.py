import unittest
from string_calculator import add,add_number,add_comma_multiple,add_newline

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(add_number("5"), 5)

    def test_two_numbers(self):
        self.assertEqual(add_comma_multiple("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(add_comma_multiple("1,2,3,4"), 10)

    def test_newline_separator(self):
        self.assertEqual(add_newline("1\n2,3"), 6)

if __name__ == "__main__":
    unittest.main()

