# Implementation of positional list adt:
#
class _DoublyLinkedBase:
    class _Node:
        __slots__ = "_element", "_next", "_prev"
        def __init__(self, _element, _next, _prev):
            self._element = _element
            self._next = _next
            self._prev = _prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_betweem(self, e, predecessor, successor):
        newest = self._Node(e, None, None)
        newest._prev = predecessor
        newest._next = successor
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._element = node._prev = node._next = None
        return element

class PositionalList(_DoublyLinkedBase):
    def __init__(self):
        pass

    def element(self):
        '''Return the element stored at the given position'''
        pass

    def first(self):
        '''Return the positon of the first element of the list. None if the element is the first element elredy'''
        pass

    def last(self):
        '''Return the position of the last element of the list. None if it is already the last position'''
        pass

    def before(self, p):
        '''Return the position just before the position p. None if it is the very first position'''
        pass

    def after(self, p):
        '''Return the position immediatly after the position p. None if it is the alredy last position'''
        pass

    def __inter__(self):
        '''Return a forward iterator for the elements of the list'''
        pass

    def add_first(self, e):
        '''Add the element e at the first position, just after the header sentinel'''
        pass

    def add_last(self, e):
        '''Add the element e at the last position, just before the trailer sentinel'''
        pass

    def add_before(self, p, e):
        '''Add the element e before the position p'''
        pass

    def add_after(self, p, e):
        '''Add the element e after the position p'''
        pass

    def replace(self, p, e):
        '''Replace the element at position p with the element e'''
        pass

    def delete(self, p):
        '''Remove and return at the position p'''
        self._delete_node(p)

