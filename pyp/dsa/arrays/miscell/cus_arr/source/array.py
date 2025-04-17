#NOTE: This is an implementation of advanced arrays using Doubly linked lists.

# Implementation of advanced arrays.
# Functions of advanced Dynamic arrays:
#     1. Instant acess of any element 
#     2. Element insertion at O(1) time complexity
#     3. Element removal at O(1) time complexity
#     4. Built in sorting methods
#     5. Iterators


# An Dynamic array implementation which has methods for advanced arrays

#FIXME: The actual problems include:
# Initialize a crawler class. Function - Crawls through the underlying python object and stores the elements by indexing them in a hash table.
# Instant sorting algorithm
# How to display the actual underlying object
# How to acess the current node in the linked list


class DynamicArrays:
    '''
    Array class for implementation of advanced dynamic arrays
    '''
    class _Node:
        __slots__ = "_element", "_next", "_prev", "_index"
        def __init__(self, element, next, previous, index):
            self._element = element
            self._next = next
            self._prev = previous
            self._index = index

    class _Hash:
        '''
        Generates a hash table and stores elements in them by assigning an index. Typically in the order of which they were appended.
        '''
        def __init__(self):
            pass
    #FIX: Initialize a hash table to store the elements and also assign them a index. In order of which they were added.

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __str__(self):
        '''
        Return the array in string format.
        '''
        #HACK: Use the hash table to view the elements in the form of a table.
        pass
    

    def __len__(self):
        '''
        Return the length of the array.
        '''
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, e):
        '''
        Add an element at the desired index. And at the last, if none provided.
        '''
        newest = self._Node(e, None, None)
        if self.is_empty():
            newest._next = self._trailer
            newest._prev = self._header
        else:
            newest._prev = self._trailer._prev
            newest._next = self._trailer
        self._size += 1

    def delete(self, i):
        '''
        Delete an element from any desired index. From the last, if none provided.
        '''
        if self.is_empty():
            raise Exception("Empty: The array is alredy empty")
        #FIX: How to delete an element from a randon position. 
        current = self._curr
        predecessor = self._curr._prev
        successor = self._curr._next
        predecessor._next = successor
        successor._prev = predecessor
        return current._element

    def instant_sort(self):
        '''
        Sort the array.
        '''
        pass

    def _resize(self, cap):
        '''
        Resize the underlying object in order to reduce memeory overhead
        '''
        pass
