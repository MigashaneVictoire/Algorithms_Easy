import unittest
import BinarySeach_main

class binarySearch_test(unittest.TestCase):
    def test_case1(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33
        expected = 3

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case2(self):
        array = [1, 5, 23, 111]
        target = 111
        expected = 3

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case3(self):
        array = [1, 5, 23, 111]
        target = 5
        expected = 1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case4(self):
        array = [1, 5, 23, 111]
        target = 35
        expected = -1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case5(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 0
        expected = 0

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case6(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 1
        expected = 1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case7(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 21
        expected = 2

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case8(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 45
        expected = 4

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case9(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 61
        expected = 6

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case10(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 71
        expected = 7

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case11(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 72
        expected = 8

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case12(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 73
        expected = 9

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case13(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 20
        expected = -1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case14(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        target = 355
        expected = 10

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case15(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355]
        target = 354
        expected = -1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case16(self):
        array = [1, 5, 23, 111]
        target = 120
        expected = -1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)

    def test_case17(self):
        array = [1, 5, 23, 111]
        target = 3
        expected = -1

        actual = BinarySeach_main.binarySearch(array, target)
        self.assertEqual(expected, actual)


if __name__=='__main__':
    unittest.main()