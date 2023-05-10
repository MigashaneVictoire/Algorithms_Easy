class Graph:
    def __init__(self, name=None):
        self.name = name
        self.children= []

    def insert(self, name):

def printTree(tree, level=0):
    if tree is not None:
        printTree(tree.right, level + 1)  # print's all the values to the left first
        print(' ' * 5 * level + '-> ' + str(tree.value))
        printTree(tree.left, level + 1)


# def test_cases():
case1 = {
    "tree": {
        "nodes": [
            {"id": "10", "left": "5", "right": "15", "value": 10},
            {"id": "15", "left": "13", "right": "22", "value": 15},
            {"id": "22", "left": None, "right": None, "value": 22},
            {"id": "13", "left": None, "right": "14", "value": 13},
            {"id": "14", "left": None, "right": None, "value": 14},
            {"id": "5", "left": "2", "right": "5-2", "value": 5},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": None, "value": 2},
            {"id": "1", "left": None, "right": None, "value": 1}
        ],
        "root": "10"
    },
    "target": 12
}

if __name__ == '__main__':
    tree = BST(int(case1["tree"]["root"]))  # get the root form the dictionary

    for key in case1["tree"]["nodes"][1:]:  # insert values in the BST
        tree.insert(key["value"])

    printTree(tree)
