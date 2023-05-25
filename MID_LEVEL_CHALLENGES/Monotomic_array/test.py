import unittest
import MonotomicArray_main as MonoArray

class MonotomicArray_test(unittest.TestCase):
    def test_case1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case2(self):
        array = []
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case3(self):
        array = [1]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case4(self):
        array = [1, 2]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case5(self):
        array = [2, 1]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case6(self):
        array = [1, 5, 10, 1100, 1101, 1102, 9001]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case7(self):
        array = [-1, -5, -10, -1100, -1101, -1102, -9001]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case8(self):
        array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case9(self):
        array = [1, 2, 0]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case10(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case11(self):
        array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case12(self):
        array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case13(self):
        array = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case14(self):
        array = [-1, -1, -1, -1, -1, -1, -1, -1]
        actual = MonoArray.isMonotonic(array)
        self.assertTrue(actual)

    def test_case15(self):
        array = [1, 2, -1, -2, -5]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case16(self):
        array = [-1, -5, 10]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case17(self):
        array = [2, 2, 2, 1, 4, 5]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case18(self):
        array = [1, 1, 1, 2, 3, 4, 1]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

    def test_case19(self):
        array = [1, 2, 3, 3, 2, 1]
        actual = MonoArray.isMonotonic(array)
        self.assertFalse(actual)

if __name__== '__main__':
    unittest.main()
