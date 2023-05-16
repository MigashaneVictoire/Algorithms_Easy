import unittest
import nthFibonacci_main as Fib


class nthFibonacci_test(unittest.TestCase):
    def test_case1(self):
        n = 6
        expected = 5
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case2(self):
        n = 1
        expected = 0
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case3(self):
        n = 2
        expected = 1
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case4(self):
        n = 3
        expected = 1
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case5(self):
        n = 4
        expected = 2
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case6(self):
        n = 5
        expected = 3
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case7(self):
        n = 7
        expected = 8
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case8(self):
        n = 8
        expected = 13
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case9(self):
        n = 9
        expected = 21
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case10(self):
        n = 10
        expected = 34
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case11(self):
        n = 11
        expected = 55
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case12(self):
        n = 12
        expected = 89
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case13(self):
        n = 13
        expected = 144
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case14(self):
        n = 14
        expected = 233
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case15(self):
        n = 15
        expected = 377
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case16(self):
        n = 16
        expected = 610
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case17(self):
        n = 17
        expected = 987
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)

    def test_case18(self):
        n = 18
        expected = 1597
        actual = Fib.getNthFib(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
