import unittest
import MoveElementToEnd_main as MoveToEnd

class MoveElementToEnd_test(unittest.TestCase):
    def test_case1(self):
        array= [2, 1, 2, 2, 2, 3, 4, 2]
        toMove= 2
        expected= [1, 3, 4, 2, 2, 2, 2, 2]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case2(self):
        array = []
        toMove =3
        expected= []
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case3(self):
        array = [1, 2, 4, 5, 6]
        toMove = 3
        expected = [1, 2, 4, 5, 6]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case4(self):
        array = [3, 1, 2, 4, 5]
        toMove = 3
        expected = [1, 2, 4, 5, 3]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case5(self):
        array =[3, 3, 3, 3, 3]
        toMove = 3
        expected = [3, 3, 3, 3, 3]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case6(self):
        array = [3, 1, 2, 4, 5]
        toMove = 3
        expected = [1, 2, 4, 5, 3]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case7(self):
        array = [1, 2, 3, 4, 5]
        toMove = 3
        expected = [1, 2, 4, 5, 3]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case8(self):
        array = [2, 4, 2, 5, 6, 2, 2]
        toMove = 2
        expected = [4, 5, 6, 2, 2, 2, 2]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case9(self):
        array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        toMove = 5
        expected = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case10(self):
        array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
        toMove = 5
        expected = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)

    def test_case11(self):
        array = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
        toMove = 5
        expected = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
        actual = MoveToEnd.moveElementToEnd(array, toMove)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()