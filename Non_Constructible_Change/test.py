from solution import nonConstructibleChange
import unittest

class testSolution(unittest.TestCase):
    def test_case_1(self):
        coins= [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        coins= [1, 1, 1, 1, 1]
        expected = 6
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        coins= [1, 5, 1, 1, 1, 10, 15, 20, 100]
        expected = 55
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        coins= [6, 4, 5, 1, 1, 8, 9]
        expected = 3
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        coins= []
        expected = 1
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        coins= [87]
        expected = 1
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        coins= [5, 6, 1, 1, 2, 3, 4, 9]
        expected = 32
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_8(self):
        coins= [5, 6, 1, 1, 2, 3, 43]
        expected = 19
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_9(self):
        coins= [1, 1]
        expected = 3
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_10(self):
        coins= [2]
        expected = 1
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_11(self):
        coins= [1]
        expected = 2
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_12(self):
        coins= [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
        expected = 87
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

    def test_case_13(self):
        coins= [1, 2, 3, 4, 5, 6, 7]
        expected = 29
        actual = nonConstructibleChange(coins)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()