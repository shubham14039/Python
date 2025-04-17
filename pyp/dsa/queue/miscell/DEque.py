#NOTE: The space complexity of this implementation is gonna be HUGE

class deq:

    DEFAULT_CAPACITY  = 12

    def __init__(self):
        self._data = [None] * deq.DEFAULT_CAPACITY
        self._size = 0
        self._front_opr = 0
        self._back_opr = 0

    def __len__(self):
        return self._size

    # def __str__(self):
    #     return str(self._data)

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        index_of_front = len(self._data)//2 - self._front_opr
        return self._data[index_of_front]

    def back(self):
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        index_of_back = len(self._data)//2 + self._back_opr
        return self._data[index_of_back]  

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = len(self._data)//2 - self._front_opr
        self._data[avail] = e
        self._size += 1
        self._front_opr += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = len(self._data)//2 +1 + self._back_opr
        self._data[avail] = e
        self._size += 1
        self._back_opr += 1

    def delete_first(self):  #FIXME: The method is not removeing any element and returning it. Also add operation to reseze the underlying array whenver the queue is shrinked
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        indeex = len(self._data)//2 - self._front_opr
        answer = self._data[indeex]
        self._data[indeex] = None
        self._size -= 1
        self._front_opr -= 1
        return answer


    def delete_last(self):  #FIXME: The method is not removeing any element and returning it. Also add operation to resize the underlying array whenever the queue is shrinked
        if self.is_empty():
            raise Exception("Empty: The queue is empty")
        indeex = len(self._data)//2 +1 + self._back_opr
        answer = self._data[indeex]
        self._data[indeex] = None
        self._size -= 1
        self._back_opr -= 1
        return answer


    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        l1 = len(self._data)//2
        l2 = len(self._data)//2 +1
        walk1 = len(old)//2
        walk2 = len(old)//2 + 1

        for _ in range(self._front_opr):
            self._data[l1] = old[walk1]
            l1 -= 1
            walk1 -= 1
        for _ in range(self._back_opr):
            self._data[l2] = old[walk2]
            l2 += 1
            walk2 += 1

        self._front = l1 - self._front_opr
        self._back  = l2 + self._back_opr
