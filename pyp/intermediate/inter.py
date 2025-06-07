# To implement a tree data structure in python, we will use nodes and pointers
# Steps:
#     1. Create a Node
#     2. Attach this node to a parent node 
#      OR 
#     1. Every node will contain an empty list 
#     2. Every child node will appended to the preferred parent node's list

class TreeNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"TreeNode({self.value})"

Root = TreeNode("A")
child1 = TreeNode("a1", Root)
child2 = TreeNode("B", Root)
child12 = TreeNode("a2", child1)

Root.add_child(child1)
Root.add_child(child2)
child1.add_child(child12)

print(Root)
print(Root.parent)
print(child12.parent)
print(TreeNode)
