from solution import sortedSquareArray
import unittest

class testSolution(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        array = [1]
        expected = [[1]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        array = [1, 2]
        expected = [[1, 4]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        array = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        array = [0]
        expected = [[0]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        array = [10]
        expected = [100]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        array = [-1]
        expected = [1]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_8(self):
        array = [-2, -1]
        expected = [1, 4]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_9(self):
        array = [-5, -4, -3, -2, -1]
        expected = [1, 4, 9, 16, 25]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_10(self):
        array = [-10]
        expected = [100]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_11(self):
        array = [-10, -5, 0, 5, 10]
        expected = [0, 25, 25, 100, 100]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_12(self):
        array = [-7, -3, 1, 9, 22, 30]
        expected = [1, 9, 49, 81, 484, 900]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_13(self):
        array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
        expected = [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_14(self):
        array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_15(self):
        array = [-1, -1, 2, 3, 3, 3, 4]
        expected = [1, 1, 4, 9, 9, 9, 16]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_16(self):
        array = [-3, -2, -1]
        expected = [1, 4, 9]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    def test_case_17(self):
        array = [-3, -2, -1]
        expected = [1, 4, 9]
        actual = sortedSquareArray(array)
        self.assertEqual(expected, actual)

    
if __name__ == "__main__":
    unittest.main()