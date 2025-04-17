# Suppose x and y are refrences to nodes of circularly linked lists, although not necessarily same list. Find a fast algorithm for telling if they belong to the same list.

class CircularList:
    class Node:
        __slots__ = "element", "next", "prev"
        def __init__(self, element, nx, prev):
            self.element = element
            self.next = nx
            self.prev = prev

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.header.next = self.header
        self.header.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size 

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise KeyError("The queue is empty")
        return self.header.next.element

    def last(self):
        if self.is_empty():
            raise KeyError("The queue is empty")
        return self.header.prev.element

    def add(self,e):
        '''Add a new element at the top. That is, just after the header. The first element becomes the second element'''
        newest = self.Node(e, None, None)
        if self.is_empty():
            self.header.next = newest
            self.header.prev = newest
            newest.prev = self.header
            newest.next = self.header
        else:
            successor = self.header.next
            newest.prev = self.header
            self.header.next = newest
            newest.next = successor
            successor.prev = newest
        self.size += 1
        print(f"Added {e}")

    def delete(self):
        '''Removes and returns the first element from the queue'''
        if self.is_empty():
            raise KeyError("The queue is empty")
        node = self.header.next
        answer = node.element
        successor = node.next
        self.header.next = successor
        successor.prev = self.header
        node.next = node.prev = node.element = None
        self.size -= 1
        return answer

    def remove(self, e):
        '''Removes the first occurance of the input element'''
        if self.is_empty():
            raise KeyError("The Queue is empty")
        temp = self.header
        while not temp.element == e:
            temp = temp.next
        predecessor = temp.prev
        successor = temp.next
        predecessor.next = successor
        successor.prev = predecessor
        temp.next = temp.prev = temp.element = None
        self.size -= 1
        print(f"Removed the element: {e}")

    def check(self, other):
        '''Check if two nodes belong to the same circular linked list'''
        pass

    def printList(self):
        if self.is_empty():
            print("The list is empty")
            return
        temp = self.header.next
        ls = []
        while temp is not self.header:
            ls.append(temp.element)
            temp = temp.next
        print(ls)

c = CircularList()
c.add(9)
c.add(8)
c.add(6)
c.add(7)
c.add(4)
print(len(c))
c.printList()
c.remove(6)
c.printList()
print(len(c))
