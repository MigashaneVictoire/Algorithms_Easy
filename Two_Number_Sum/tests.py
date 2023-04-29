from my_solution import twoNumberSum
import unittest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 10
        expected = [-1, 11]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    
if __name__ == "__main__":
    unittest.main()