from Validate_Subsequence_solution import isValidSubsequence
import unittest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 25, 6, -1, 8, 10]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 6, -1, 8, 10]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [26]
        expected = False
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, 10]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 10]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 25, 22, 6, -1, 8, 10]
        expected = False
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_8(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [25]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_9(self):
        array = [1, 1, 1, 1, 1]
        sequence = [1, 1, 1]
        expected = True
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

    def test_case_10(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]
        expected = False
        actual = isValidSubsequence(array, sequence)
        self.assertEqual(expected, actual)

 
if __name__ == "__main__":
    unittest.main()