from solution import sortedSquareArray
import unittest

class testSolution(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main()