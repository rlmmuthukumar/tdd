import unittest
from string_calculator import add,add_number,add_comma_multiple,add_newline,add_custom,add_negative

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

    def test_custom_delimiter(self):
        self.assertEqual(add_custom("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add_negative("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negatives not allowed: -2, -4")   

if __name__ == "__main__":
    unittest.main()

