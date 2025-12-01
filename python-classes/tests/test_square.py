#!/usr/bin/python3
import unittest

Square = __import__('6-square').Square

class TestSquareTaskSix(unittest.TestCase):
    def test_SizeIsPos(self):
        with self.assertRaises(ValueError):
            Square(-3)
    def test_SizeIsNotInt(self):
        with self.assertRaises(TypeError):
            Square("hello")
    def test_PositionIsNotTup(self):
        with self.assertRaises(TypeError):
            Square(0, [1, 2])
    def test_PositionHasTwoElements(self):
        with self.assertRaises(TypeError):
            Square(0, (1, 2, 3))
    def test_PositionIsTupleOfTwoInts(self):
        with self.assertRaises(TypeError):
            Square(0, ("hello", "world"))

if __name__ == "__main__":
    unittest.main()
