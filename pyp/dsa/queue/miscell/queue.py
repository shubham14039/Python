class ArrayQueue:
    '''
    FIFO queue implemenatation with list as an underlying storage
    '''
    DEFAULT_CAPACITY = 10

    def __init__(self):
        '''
        Create an empty queue
        '''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0  # self._size is the current size of the queue ADT, we cant use len() function as it will give the total length of the underlying array. Which is not the case.
        self._front = 0  # self._front is the index of the first element 
        # self._back = -1
    #
    # def __str__(self):
    #     '''
    #     Return the string format of the data. Not the actual queue, but the underlying array ADT
    #     '''
    #     return str(self._data)

    def __len__(self):
        '''
        Return the length of the queue
        '''
        return self._size  # Now if we use the len function, it will return the size of the array which is actually filled by elements. (The rest are filled by None items )

    def is_empty(self):
        '''
        Return True if the queue is empty
        '''
        return self._size == 0

    def first(self):
        '''
        Return (but do not remove) the element at the front
        Raise Empty Exception if the queue is empty
        '''
        if self.is_empty():
            raise Exception('The queue is empty')
        return self._data[self._front]

    def deque(self):
        '''
        Remove and return the first element of the queue
        Raise Empty Exceptyon if the queue is empty
        '''
        if self.is_empty():
            raise Exception('The queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None

        self._front = (self._front + 1) % len(self._data)

        #NOTE: The modulo operator and hence len(self._data) ensures that the indexing does not go beoyond the bounds of the underlying array. In that case, the index wraps around.
        self._size -= 1  # decrease the size by one. the actual length of the underlying array remains the same, it is just that the the position of the popped item is refrenced to None. 

        #FIXME: The maximum capacity of the queue depends on the number of elements that have ever been stored in the underlying array. This causes an inefficiency of space complexity, which is O(n).

        #HACK: In order to tackle this, following lines of code have been added

        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)

        return answer 

    def enque(self, e):
        '''
        Add an element at the back of the queue
        '''
        if self._size == len(self._data):  # If the underlying array is already filled, then double the array size (Dynamic arrays)
            self._resize(2*len(self._data))

        avail = (self._size + self._front) % len(self._data)   

        self._data[avail] = e  # Assign the newcoming element to the last index. 
        self._size += 1  # Increase the size of the queue by 1. 


# TODO: Explain the working of the resize method below


    def _resize(self, cap):
        '''
        Resize to a new list of capacity >= len(self)
        '''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k]  = old[walk]
            walk = (1+ walk)%len(old)
        self._front = 0 

