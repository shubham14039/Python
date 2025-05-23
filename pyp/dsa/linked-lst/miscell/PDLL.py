# Implementation of a positional linked list

class _DoublyLinkedBase:
    '''
    A base class providing a doubly linked list representation
    '''
    class _Node:
        '''
        initiate the node fields inside
        '''
        __slots__ = "_element", "_prev", "_next"
        def __init__(self, element, prev, next):
            '''
            create an empty list
            '''
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        '''
        create an empty list
        '''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        '''
        returns the number of elements in the list
        '''
        return self._size

    def is_empty(self):
        '''
        Return True if the list is empty
        '''
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''
        Add an element between two existing nodes and return the inserted node
        '''
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''
        Delete non essential node from the list and return its element
        '''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        el = node._element
        node._next = node._prev = node._element = None
        return el

class PositionalList(_DoublyLinkedBase):
    '''
    A sequential container of elements allowing positional acess
    '''
    class Position:
        '''
        An abstraction representing the location of a single element
        '''
        def __init__(self, container, node):
            '''
            Constructor should not be invoked by the user
            '''
            self._container = container
            slef._node = node

        def element(self):
            '''
            Return the element stored in this position 
            '''
            return self._node._element

        def __eq__(self, other):
            '''
            Return True if other is a position representing the same location
            '''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''
            Return True if other does not represent the same location
            '''
            return not (self == other)

    def _validate(self, p):
        '''
        Return position's node, or raise appropriate error
        '''
        if not isinstance(p, self.Position): 
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        '''
        Return position instance for the given node (None if sentinel)
        '''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        '''
        Return the first position of the list (None if empty)
        '''
        return self._make_position(self._header._next)

    def last(self):
        '''
        Return the last position of the list (None if empty)
        '''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''
        Return the position just before the position p, (None if p is first)
        '''
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        '''
        Return the position just after the position p, (None if p is last)
        '''
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        '''
        Generate a forward iteration of the element in the list
        '''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        '''
        Add element between the existing nodes and return the position
        '''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        '''
        Insert element e at the front of the list and return the new position. 
        '''
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''
        Insert element e at the last of the list and return the new position. 
        '''
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p , e):
        '''
        Insert element e into list before position p and return the new position
        '''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''
        Insert element e into list after position p and return the new position
        '''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        '''
        Remove and return the element at position p
        '''
        original = self._validate(p)
        return self._delete_node(original)

    def relplace(self, p, e):
        '''
        Replace the element at position p with e
        Return the element formerly at position p.
        '''
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
