import unittest
import minimumWaitingTime_main as waitTime

class minimumWaitingTime_test(unittest.TestCase):
    def test_case1(self):
        queries= [3, 2, 1, 2, 6]
        expected = 17
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case2(self):
        queries = [2, 1, 1, 1]
        expected = 6
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case3(self):
        queries = [1, 2, 4, 5, 2, 1]
        expected = 23
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case4(self):
        queries = [25, 30, 2, 1]
        expected = 32
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case5(self):
        queries = [1, 1, 1, 1, 1]
        expected = 10
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case6(self):
        queries = [7, 9, 2, 3]
        expected = 19
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case7(self):
        queries = [4, 3, 1, 1, 3, 2, 1, 8]
        expected = 45
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case8(self):
        queries = [2]
        expected = 0
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case9(self):
        queries = [7]
        expected = 0
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case10(self):
        queries = [8, 9]
        expected = 8
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case11(self):
        queries = [1, 9]
        expected = 1
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case12(self):
        queries = [5, 4, 3, 2, 1]
        expected = 20
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case13(self):
        queries = [1, 2, 3, 4, 5]
        expected = 20
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case14(self):
        queries = [1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1]
        expected = 81
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)

    def test_case15(self):
        queries = [17, 4, 3]
        expected = 10
        actual = waitTime.minimumWaitingTime(queries)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()