# Let's make our own array data type. That too in python

import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0 
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        '''
        Returns the length of the array. Not the underlying data structure.
        '''
        return self._n

    def __getitem__(self, k):
        '''
        Return the element at the index k
        '''
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]

    def appen(self, obj):
        '''
        Add object at the end of the array
        '''
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def rmv_in(self):
        '''
        Removes any item from the list
        '''
        pass

    def rmv(self):
        '''
        Removes the last item from the list
        '''
        pass

    def _resize(self, cap):
        '''
        Used to resize the underlying data structure. Which is written in C btw.
        '''
        b = self._make_array(cap)
        for k in range(self._n):
            b[k] = self._A[k]
        self._A = b
        self._capacity = cap

    def _make_array(self, c):
        '''
        A wrapper written in C, used to return a new array with capacity c.
        '''
        return (c*ctypes.py_object)()

a = DynamicArray()
a.appen(8)
print(len(a))
