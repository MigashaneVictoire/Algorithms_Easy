import unittest
import classPhotos_main as Photos

class minimumWaitingTime_test(unittest.TestCase):
    def test_case1(self):
        blueShirtHeights = [6, 9, 2, 4, 5]
        redShirtHeights = [5, 8, 1, 3, 4]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected ,actual)

    def test_case2(self):
        blueShirtHeights = [5, 8, 1, 3, 4]
        redShirtHeights = [6, 9, 2, 4, 5]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case3(self):
        blueShirtHeights = [5, 8, 1, 3, 4, 9]
        redShirtHeights = [6, 9, 2, 4, 5, 1]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case4(self):
        blueShirtHeights = [6]
        redShirtHeights = [6]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case5(self):
        blueShirtHeights = [125]
        redShirtHeights = [126]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case6(self):
        blueShirtHeights =  [2, 3, 4, 5, 6]
        redShirtHeights = [1, 2, 3, 4, 5]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case7(self):
        blueShirtHeights = [5, 6, 7, 2, 3, 1, 2, 3]
        redShirtHeights = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case8(self):
        blueShirtHeights = [2, 2, 2, 2, 2, 2, 2, 2]
        redShirtHeights = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case9(self):
        blueShirtHeights = [126]
        redShirtHeights = [125]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case10(self):
        blueShirtHeights = [21, 5, 4, 4, 4, 4, 4, 4, 4]
        redShirtHeights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case11(self):
        blueShirtHeights = [20, 5, 4, 4, 4, 4, 4, 4]
        redShirtHeights = [19, 19, 21, 1, 1, 1, 1, 1]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case12(self):
        blueShirtHeights = [2, 4, 7, 5, 1]
        redShirtHeights = [3, 5, 6, 8, 2]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case13(self):
        blueShirtHeights = [2, 4, 7, 5, 1, 6]
        redShirtHeights = [3, 5, 6, 8, 2, 1]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case14(self):
        blueShirtHeights = [5, 4]
        redShirtHeights = [4, 5]
        expected = False
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)

    def test_case15(self):
        blueShirtHeights = [5, 4]
        redShirtHeights = [5, 6]
        expected = True
        actual = Photos.classPhotos(redShirtHeights, blueShirtHeights)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()