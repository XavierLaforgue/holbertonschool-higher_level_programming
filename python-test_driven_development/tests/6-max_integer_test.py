#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_EmptyInput(self):
        self.assertIsNone(max_integer())
    def test_EmptyList(self):
        self.assertIsNone(max_integer([]))
    def test_IntUnsortedList(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_SingleElementList(self):
        self.assertEqual(max_integer([1]), 1)
    def test_NegativeIntSortedList(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
    def test_PosAndNegIntUnsortedList(self):
        self.assertEqual(max_integer([-1, 3, -4, 8, -10, 0]), 8)
    def test_PositiveIntSortedList(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_IntSortedReversedList(self):
        self.assertEqual(max_integer([15, 10, 4, 3, 0, -45]), 15)
    def test_RepeatedIntUnsortedList(self):
        self.assertEqual(max_integer([1, 2, 5, 2, 6, 3, 1, 5]), 6)
    def test_FloatInList(self):
        self.assertEqual(max_integer([1.0, 2.4, 5.5, 2.0, 6, 3, 1, 5]), 6)
    def test_StringInList(self):
        with self.assertRaises(TypeError):
            max_integer([4.3, "hello", 2, 5, 10])
    def test_String(self):
        self.assertEqual(max_integer("hello"), "o")
    def test_InputIsNone(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
