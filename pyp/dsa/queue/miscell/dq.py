
class dq:

    DEFAULT_CAPACITY = 12
    
    def __init__(self):
        self._data = [None] * dq.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    # def __str__(self):
    #     return str(self._data)

    def __len__(self):
        return self._size

    def is_empty(self):
        return  self._size == 0 

    def first(self):
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        back = (self._front + self._size -1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1 

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

    def delete_first(self):
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def delete_last(self):
        back = (self._front + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
