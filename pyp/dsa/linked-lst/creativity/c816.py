# Give a recursive implementation of singly linked list class, such that an instance of a non empty list stores its first element and a refrence to alist of next elements

class SinglyList:
    class _Node:
        def __init__(self, element, nx):
            self.element = element
            self.next = nx

    def __init__(self, tail = None):
        self.head = self._Node(None, None)
        self.tail = tail
        # self.tail is being used as a refrencing item for the next linked list object
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, e):
        newest = self._Node(e, None)
        self.size += 1

