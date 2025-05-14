#!/usr/bin/python3
import unittest

safe_print_integer = __import__("1-safe_print_integer").safe_print_integer

class TestSafePrintInt(unittest.TestCase):
    def test_ints(self):
        self.assertTrue(safe_print_integer(-10))
        self.assertTrue(safe_print_integer(10))
        self.assertTrue(safe_print_integer(0))
        self.assertTrue(safe_print_integer(9))
        self.assertTrue(safe_print_integer(25))
        self.assertTrue(safe_print_integer(-327))
        self.assertTrue(safe_print_integer(1228573))

    def test_strings(self):
        self.assertFalse(safe_print_integer("10"))
        self.assertFalse(safe_print_integer("hello"))
        self.assertFalse(safe_print_integer("not printed"))

    def test_floats(self):
        self.assertFalse(safe_print_integer(3.14))
        self.assertFalse(safe_print_integer(1/2))
        self.assertFalse(safe_print_integer(0.69))

    def test_ListsTuplesSequence(self):
        self.assertFalse(safe_print_integer([1, 3]))
        self.assertFalse(safe_print_integer((2, 4)))
        self.assertFalse(safe_print_integer(range(4)))

if __name__ == "__main__":
    unittest.main()
