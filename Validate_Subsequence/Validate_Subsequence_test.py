from Validate_Subsequence_solution import isValidSubsequence
import unittest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

if __name__ == "__main__":
    unittest.main()