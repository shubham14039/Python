# Develop a python program to reverse the elements of a given queue.

class queue:

    def __init__(self):
        self._data = []
        self._front = 0  #self._front is the index of the element at the front 

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        #Return the first ellement of the queue
        if self.is_empty():
            raise Exception("The queue is empty")
        return self._data[self._front]

    def enque(self, e):
        #Enqueue a new element at the back of the queue
        self._data.append(e)

    def deque(self):
        #Dequeue the last added element from the queue.
        if self.is_empty():
            raise Exception("The queue is empty")
        answer = self._data[self._front]
        self._data.pop()
        return answer

    def reverse_queue(self):
        #Reverse the elements of the queue
        pass

# How do we reverse a queue (with array as its underlying data structure), using only the allowed functions or methods.
#     steps:
# 1. use of recursion:
#     deque the first ellement and use recursion to reverse the rest of the queue, and enque the dequed ellement,
