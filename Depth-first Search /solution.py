# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name)) # add root node as child
        return self

    def depthFirstSearch(self, array): # self is acting as the tree
        # Write your code here.
        array.append(self.name) # record node.valaue in new array
        for child in self.children: # per child of node.valaue added in new array
            child.depthFirstSearch(array) # DFS on child
        return array
