import unittest

safe_print_list = __import__("0-safe_print_list").safe_print_list

class TestSafePrint(unittest.TestCase):

    def test_ExpectedReturn(self):
        self.assertEqual(safe_print_list([1, 2, 3], 3), 3)
        self.assertEqual(safe_print_list([1, 2, 3], 5), 3)
        self.assertEqual(safe_print_list([1, 2, 3], 1), 1)
        self.assertEqual(safe_print_list([1, 2, 3, 5, 10], 1), 1)
        self.assertEqual(safe_print_list([1, 2, 3, 5, 10], 5), 5)
    def test_WorksWithNonInts(self):
        self.assertEqual(safe_print_list([1, "hello", 3], 3), 3)
        self.assertEqual(safe_print_list([1, 4.5, safe_print_list()], 5), 3)

if __name__ == "__main__":
    unittest.main()
