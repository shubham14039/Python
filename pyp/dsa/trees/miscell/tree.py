
class Tree:
    # Abstract base class for implementing a tree structure
    class position:
        # An abstraction representing the location of a single element
        def element(self):
            '''Return the element stored at this position'''
            raise NotImplementedError("Must be implemented by the subclass")

        def __eq__(self, other):
            '''Return if other position represents the same location'''
            raise NotImplementedError("Must be implemented by the subclass")

        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not (self == other)

    def root(self):
        '''Return the postion representing the trees' root (None if empty)''' 
        raise NotImplementedError("Must be implemented by the subclass")

    def parent(self, p):
        raise NotImplementedError("Must be implemented by the subclass")

    def num_children(self, p):
        raise NotImplementedError("Must be implemented by the subclass")

    def children(self, p):
        raise NotImplementedError("Must be implemented by the subclass")

    def __len__(self):
        raise NotImplementedError("Must be implemented by the subclass")

