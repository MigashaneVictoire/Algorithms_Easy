import unittest
import BranchSums as BS
import unorderedTree_construction as NonOrderTree

class BranchSumsTesting(unittest.TestCase):
    def test_case_1(self):
        case = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": "6", "right": "7", "value": 3},
                    {"id": "4", "left": "8", "right": "9", "value": 4},
                    {"id": "5", "left": "10", "right": None, "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9},
                    {"id": "10", "left": None, "right": None, "value": 10}
                ],
                "root": "1"
            }
        }

        tree = NonOrderTree.TreeAsc(int(case["tree"]["root"]))
        for key in case["tree"]["nodes"][1:]:
            tree.Insert(key["value"])

        expected = [15, 16, 18, 10, 11]
        actual = BS.BranchSums(tree)
        message = f"expected: {expected} != actual: {actual}"

        self.assertEqual(expected, actual, message)


if __name__ == '__main__':
    unittest.main()
