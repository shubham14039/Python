# Implementation of a doubly circular linked list
#NOTE: Write a function to reverse the linked list.

class _DoublyLinkedBase:

    class _Node:

        __slots__ = "_element", "_prev", "_next"
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._trailer = self._Node(None, None, None)
        self._trailer._prev = self._trailer
        self._trailer._next = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._next = node._prev = node._element = None
        return element


class CircularQueue(_DoublyLinkedBase):

    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def is_full(self):
        return self._size == self._capacity

    def front(self):
        if self.is_empty():
            return "Empty: The circular queue is empty"
        front_element = self._trailer._next._element
        return front_element

    def rear(self):
        if self.is_empty():
            return "Empty: The circular queue is empty"
        rear_element = self._trailer._prev._element
        return rear_element

    def enque(self, e):
        if self.is_full():
            return "Circular queue already full"
        if self.is_empty():
            return self._insert_between(e, self._trailer, self._trailer)
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def deque(self):
        if self.is_empty():
            return "Empty: The circular queue is empty"
        return self._delete_node(self._trailer._next)


cq = CircularQueue(5)

# Fill the queue
cq.enque(1)
cq.enque(2)
cq.enque(3)
cq.enque(4)
cq.enque(5)
print("Queue full:", cq.is_full())  # Expected: True

# Dequeue two elements and enqueue again to test wrapping around
print("Dequeue (expected: 1):", cq.deque())  # Expected: 1
print("Dequeue (expected: 2):", cq.deque())  # Expected: 2
cq.enque(6)
cq.enque(7)
print("Queue full after wrap around (expected: True):", cq.is_full())  # Expected: True
print("Front element (expected: 3):", cq.front())  # Expected: 3
print("Rear element (expected: 7):", cq.rear())  # Expected: 7
print("STAGE 01 COMPLETED\n")


cw = CircularQueue(4)

# Interleaved enqueue and dequeue
cw.enque(10)
print("Front (expected: 10):", cw.front())  # Expected: 10
cw.enque(20)
print("Dequeue (expected: 10):", cw.deque())  # Expected: 10
cw.enque(30)
print("Front (expected: 20):", cw.front())  # Expected: 20
cw.enque(40)
cw.enque(50)
print("Queue full (expected: True):", cw.is_full())  # Expected: True
print("Dequeue (expected: 20):", cw.deque())  # Expected: 20
cw.enque(60)
print("Rear (expected: 60):", cw.rear())  # Expected: 60
print("STAGE 02 COMPLETED\n")


ce = CircularQueue(3)

# Test empty state
print("Queue empty initially (expected: True):", ce.is_empty())  # Expected: True

# Fill the queue and test full state
ce.enque(1)
ce.enque(2)
ce.enque(3)
print("Queue full (True):", ce.is_full())  # Expected: True

# Dequeue all elements and check empty state
print("Dequeue (expected: 1):", ce.deque())  # Expected: 1
print("Dequeue (expected: 2):", ce.deque())  # Expected: 2
print("Dequeue (expected: 3):", ce.deque())  # Expected: 3
print("Queue empty after all dequeues (expected: True):", ce.is_empty())  # Expected: True

# Attempt to dequeue from empty queue
print("Dequeue on empty queue (expected: Empty: The circular queue is empty):", ce.deque())  # Expected: "Queue is empty"
print("STAGE 03 COMPLETED\n")


cr = CircularQueue(1000)

# Enqueue maximum elements
for i in range(1000):
    cr.enque(i)
print("Queue full after max enqueues (expected: True):", cr.is_full())  # Expected: True

# Dequeue half and enqueue again to check performance with large input
for _ in range(500):
    cr.deque()
for i in range(500, 1000):
    cr.enque(i)
print("Queue full after wrap around at max capacity (expected: True):", cr.is_full())  # Expected: True
print("STAGE 04 COMPLETED\n")


ct = CircularQueue(1)

ct.enque(42)
print("Front after single enqueue (expected: 42):", ct.front())  # Expected: 42
print("Rear after single enqueue (expected: 42):", ct.rear())  # Expected: 42
print("Queue full (expected: True):", ct.is_full())  # Expected: True
print("Dequeue single element (expected: 42):", ct.deque())  # Expected: 42
print("Queue empty after single dequeue (expected: True):", ct.is_empty())  # Expected: True
print("STAGE 05 COMPLETED\n")
