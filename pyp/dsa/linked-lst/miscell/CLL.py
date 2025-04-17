#NOTE: Write a function to reverse the linked list.

class CircularLinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Empty: The circular queue is empty")
        head = self._tail._next
        return head._element

    def enque(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest #FIX: Why newest is assigned as the tail onject
        self._size += 1

    def deque(self):
        if self.is_empty():
            raise Exception("Empty: The circular queue is empty")
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        self._tail._next = head._next
        self._size -= 1
        return head._element

    def rotate(self):
        '''
        Used for rotating the queue externally
        '''
        if self._size > 0:
            self._tail = self._tail._next

    def queue(self):
        current = self.first
        queue_elements = []
        while current:
            queue_elements.append(current._element)
            current = current._next
        return queue_elements

