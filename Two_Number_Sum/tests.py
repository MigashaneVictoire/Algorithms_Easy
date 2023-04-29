from my_solution import twoNumberSum
import unittest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 10
        expected = [-1, 11]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        array = [4, 6]
        targetSum = 10
        expected = [4, 6]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        array = [4, 6, 1]
        targetSum = 5
        expected = [4, 1]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(sorted(expected), actual)

    def test_case_4(self):
        array = [4, 6, 1, -3]
        targetSum = 3
        expected = [-3, 6]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        targetSum = 17
        expected = [8, 9]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        targetSum = 18
        expected = [3, 15]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        array = [-7, -5, -3, -1, 0, 1, 3, 5, 7]
        targetSum = -5
        expected = [-5, 0]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_8(self):
        array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
        targetSum = 163
        expected = [-47, 210]
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_9(self):
        array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
        targetSum = 164
        expected = []
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_10(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        targetSum = 15
        expected = []
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_11(self):
        array = [14]
        targetSum = 15
        expected = []
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    def test_case_12(self):
        array = [15]
        targetSum = 15
        expected = []
        actual = twoNumberSum(array, targetSum)
        self.assertEqual(expected, actual)

    
if __name__ == "__main__":
    unittest.main()