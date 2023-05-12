import collections
class unorderedTree:
    def __init__(self, value):
        self.children = []
        self.value = value

    def Insert(self, value):
        self.children.append(unorderedTree(value))
        return self
    def breadthFirstSearch(self, array):
        N = collections.deque([self])
        while N:

def printTree(Tree, level = 0):
    if Tree is not None:
        printTree(Tree.right, level + 1)
        print(" " * 4 * level + "-> " + str(Tree.value))
        printTree(Tree.left, level + 1)

AlgoTree = {
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

if __name__ == "__main__":
    Tree = unorderedTree(int(AlgoTree["tree"]["root"]))

    for key in AlgoTree["tree"]["nodes"][1:]:
        Tree.Insert(key["value"])

    printTree(Tree)
