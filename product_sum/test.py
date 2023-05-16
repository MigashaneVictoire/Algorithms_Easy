import unittest
import productSum_main


class ProductSum_test(unittest.TestCase):
    def test_case1(self):
        array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        expected = 12
        actual = productSum_main.productSum(array)
        self.assertEqual(expected, actual)

    def test_case2(self):
        array = [1, 2, 3, 4, 5]
        expected = 15
        actual = productSum_main.productSum(array)
        self.assertEqual(expected, actual)

    def test_case3(self):
        array = [1, 2, [3], 4, 5]
        expected = 18
        actual = productSum_main.productSum(array)
        self.assertEqual(expected, actual)

    def test_case4(self):
        array = [
    [1, 2],
    3,
    [4, 5]
  ]
        expected = 27
        actual = productSum_main.productSum(array)
        self.assertEqual(expected, actual)

    def test_case5(self):
        array = [
    [
      [
        [
          [5]
        ]
      ]
    ]
  ]
        expected = 600
        actual = productSum_main.productSum(array)
        self.assertEqual(expected, actual)

    def test_case6(self):
        array = [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]
        expected = 1351
        actual = productSum_main.productSum(array)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()