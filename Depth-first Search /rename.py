import unittest
from DepthFirstSearch_main import Node
from GraphConstraction import Graph

class DepthFirstSearch_test(unittest.TestCase):
    def test_case1(self):
        array=
        expected = ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
        actual = Node.depthFirstSearch(array)
        self.assertEqual(expected, actual)

if __name__ =='__main__':
    unittest.main()