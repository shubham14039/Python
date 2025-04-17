# Describe a non recursive metho to find the middle node of a linked list. This method should only use link hopping and not any counter method. In case of even number of nodes, return the node next to the "middle" of the linked list. What is the time complexity of the method


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next

if __name__ == "__main__":
    c1 = LinkedList()
    c1.head = Node(9)
    second = Node(8)
    third = Node(7)
    c1.head.next = second
    second.next = third
    c1.traverse()
