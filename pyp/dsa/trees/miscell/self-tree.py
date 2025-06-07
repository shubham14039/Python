# Implementstion of tree data structure

# Items in a baisc tree:
#     Root
#     Parent
#     Child
#     siblings
class TreeNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def parent(self):
        return self.parent

    def siblings(self):
        up = self.parent
        return up.children

    def children(self):
        return self.children

    def child(self, child):
        return True if child in self.children else False

    def Root(self):
        up = self.parent
        while up is not None:
            up = up.parent
        return up

    def __repr__(self):
        return f"TreeNode ({self.value})"

R = TreeNode("A")
child1 = TreeNode("B", R)
child2 = TreeNode("C", R)
child3 = TreeNode("D", R)
child4 = TreeNode("E", child1)
child5 = TreeNode("Y", child3)

R.add_child(child1)
R.add_child(child2)
R.add_child(child3)
child1.add_child(child4)
child3.add_child(child5)

print(R.children())
