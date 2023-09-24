import unittest
from unittest.mock import patch

from is_even import *


class TestIsEvenMethods(unittest.TestCase):
    def test_intended_method(self):
        self.assertFalse(intended_method(5))
        self.assertTrue(intended_method(-42))
        self.assertFalse(intended_method(12345))

    def test_bitwise_method(self):
        self.assertFalse(bitwise_method(5))
        self.assertTrue(bitwise_method(-42))
        self.assertFalse(bitwise_method(12345))

    def test_string_method(self):
        self.assertFalse(string_method(5))
        self.assertTrue(string_method(-42))
        self.assertFalse(string_method(12345))

    def test_recursive_method(self):
        self.assertFalse(recursive_method(5))
        self.assertTrue(recursive_method(-42))
        self.assertFalse(recursive_method(12345))

    def test_loop_method(self):
        self.assertFalse(loop_method(5))
        self.assertTrue(loop_method(-42))
        self.assertFalse(loop_method(12345))

    def test_switch_method(self):
        self.assertFalse(switch_method(5))
        self.assertTrue(switch_method(-42))
        self.assertFalse(switch_method(12345))

    def test_range_method(self):
        self.assertFalse(range_method(5))
        self.assertTrue(range_method(-42))
        self.assertFalse(range_method(12345))

    def test_fast_range_method(self):
        self.assertFalse(fast_range_method(5))
        self.assertTrue(fast_range_method(-42))
        self.assertFalse(fast_range_method(12345))

    @patch("builtins.input", side_effect=["n", "y", "n"])
    def test_input_method(self, _):
        self.assertFalse(input_method(5))
        self.assertTrue(input_method(-42))
        self.assertFalse(input_method(12345))

    def test_hardcoded_method(self):
        self.assertFalse(hardcoded_method(5))
        self.assertTrue(hardcoded_method(-42))
        self.assertFalse(hardcoded_method(12345))

    def test_convince_method(self):
        self.assertFalse(convince_method(5))
        self.assertTrue(convince_method(-42))
        self.assertFalse(convince_method(12345))


if __name__ == "__main__":
    unittest.main()
