# test_roman_to_int_func.py

import unittest
roman_to_int = __import__("12-roman_to_int").roman_to_int

class TestRomanToIntConverter(unittest.TestCase):

    def test_badinput(self):
        self.assertEqual(roman_to_int(""), 0)
        self.assertEqual(roman_to_int([]), 0)
        self.assertEqual(roman_to_int(None), 0)
        self.assertEqual(roman_to_int(5), 0)
        self.assertEqual(roman_to_int(3.4), 0)
        self.assertEqual(roman_to_int(["I", "V"]), 0)

    def test_romanchar(self):
        self.assertEqual(roman_to_int("Q"), -1)
        self.assertEqual(roman_to_int("W"), -1)
        self.assertEqual(roman_to_int("E"), -1)

    def test_singlechar(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)

    def test_badrepetitionsyntax(self):
        self.assertEqual(roman_to_int("VV"), -1)
        self.assertEqual(roman_to_int("LLL"), -1)
        self.assertEqual(roman_to_int("IIII"), -1)
        self.assertEqual(roman_to_int("XXXXX"), -1)

    def test_romanrepetitionsyntax(self):
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("XX"), 20)
        self.assertEqual(roman_to_int("CC"), 200)
        self.assertEqual(roman_to_int("MMM"), 3000)

    def test_romansubstractionsyntax(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XIV"), 14)
        self.assertEqual(roman_to_int("XIX"), 19)
        self.assertEqual(roman_to_int("XL"), 40)
        self.assertEqual(roman_to_int("CD"), 400)
        self.assertEqual(roman_to_int("LXXXIX"), 89)
    
    def test_badsubstractionsyntax(self):
        self.assertEqual(roman_to_int("VX"), -1)
        self.assertEqual(roman_to_int("VL"), -1)
        self.assertEqual(roman_to_int("LC"), -1)
        self.assertEqual(roman_to_int("XIIX"), -1)
        self.assertEqual(roman_to_int("XXL"), -1)
        self.assertEqual(roman_to_int("XXXD"), -1)
        self.assertEqual(roman_to_int("IXXX"), -1)

    def test_twochars(self):
        self.assertEqual(roman_to_int("II"), 2)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("VI"), 6)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XI"), 11)
        self.assertEqual(roman_to_int("XV"), 15)
        self.assertEqual(roman_to_int("XX"), 20)
        self.assertEqual(roman_to_int("LX"), 60)

    def test_threechars(self):
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("VII"), 7)
        self.assertEqual(roman_to_int("XII"), 12)
        self.assertEqual(roman_to_int("XVI"), 16)
        self.assertEqual(roman_to_int("XIX"), 19)
        self.assertEqual(roman_to_int("XIX"), 19)
        self.assertEqual(roman_to_int("LIV"), 54)
        self.assertEqual(roman_to_int("CXX"), 120)
        self.assertEqual(roman_to_int("CDL"), 450)

    def test_fourchars(self):
        self.assertEqual(roman_to_int("VIII"), 8)
        self.assertEqual(roman_to_int("XIII"), 13)
        self.assertEqual(roman_to_int("XVII"), 17)
        self.assertEqual(roman_to_int("XXII"), 22)
        self.assertEqual(roman_to_int("XXIV"), 24)
        self.assertEqual(roman_to_int("LVI"), 56)

    def test_lowercase(self):
        self.assertEqual(roman_to_int("viii"), 8)
        self.assertEqual(roman_to_int("Xiii"), 13)
        self.assertEqual(roman_to_int("xvii"), 17)
        self.assertEqual(roman_to_int("xxii"), 22)
        self.assertEqual(roman_to_int("lvi"), 56)
        self.assertEqual(roman_to_int("vx"), -1)
        self.assertEqual(roman_to_int("vl"), -1)
        self.assertEqual(roman_to_int("lc"), -1)

if __name__ == "__main__":
    unittest.main()
