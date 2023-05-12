class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def BranchSums(tree):
    sums = []
    BranchSumsHelper(tree, 0, sums)
    return sums


def BranchSumsHelper(tree, runningSum, sums):
    if tree is None:
        return

    newSum = runningSum + tree.value
    if tree.left is None and tree.right is None:
        sums.append(newSum)
        return
    BranchSumsHelper(tree.left, newSum, sums)
    BranchSumsHelper(tree.right, newSum, sums)

