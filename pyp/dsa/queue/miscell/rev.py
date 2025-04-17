# Implementation of a double ended queue

class DEque:
    '''Implementation of a double ended queue, which follows both FIFO and LIFO principles'''
    DEFAULT_CAPACITY = 12
    def __init__(self):
        self._data = [None] * DEque.DEFAULT_CAPACITY
        self._front = None  #NOTE: This is the index of the element at the front
        self._back = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0 

    def first(self):
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        else:
            return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        else:
            return self._data[self._back]

    def enque_first(self, e):
        '''Enque from the first position '''
        if self._size == len(self._data):
            self._resize(2*self._size)
        #index of the new element if there is available sapce
        avail = 
        if self.is_empty():
            self._front = avail
        self._data[avail] = e
        self._size += 1

    def deque_first(self):
        '''Deque from the first position '''
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        answer = self._data[self._front]
        self._front = #New self._front, which is next of previous one

        self._size -= 1
        return answer

    def enque_last(self, e):
        '''Enque from the first position '''
        if self._size == len(self._data):
            self._resize(2*self._size)
        avail = 
        if self.is_empty():
            self._back = avail
        self._data[avail] = e
        self._size += 1

    def deque_last(self):
        '''Deque from the last'''
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        answer = self._data[self._back]
        self._back = #New self._back
        self._size -= 1
        return answer

    def _resize(self, cap):
        current = self._data
        new = [None]*cap

