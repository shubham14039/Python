# Write a program that inserts a new node in circular linked list at a position entered by the user.

class Circular_list:
    class _Node:
        def __init__(self, element, n, p):
            self.element = element
            self.next = n
            self.prev = p

    def __init__(self):
        self.header = self._Node(None, None, None)
        self.trailer = self._Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.next = self.header
        self.header.prev = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        '''Returns the lenghth of the linked list'''
        return self.size

    def is_empty(self):
        '''Returns True if the list is empty'''
        return self.size == 0

    def add(self,e):
        '''Adds a new element at the end'''
        newest = self._Node(e, None, None)
        predecessor = self.trailer.prev
        newest.next = self.trailer
        newest.prev = predecessor
        predecessor.next = newest
        self.trailer.prev = newest
        self.size += 1

    def delete(self):
        '''Removes and returns one element from the last'''
        if self.is_empty():
            raise ValueError("The list is empty")
        current = self.trailer.prev
        ans = current.element
        predecessor = current.prev
        predecessor.next = self.trailer
        self.trailer.prev = predecessor
        current.element = current.next = current.prev = None
        self.size -= 1
        return ans

    def __find__(self, n):
        '''Find the node given its position as integer'''
        if self.is_empty():
            raise ValueError("The list is empty")
        if self.size < n:
            raise IndexError("Index greater than the size itself")
        else:
            temp = self.header.next
            x = 1
            while x < n:
                temp = temp.next
                x += 1
            return temp

    def insert(self, e, n):
        '''Inserts a new element at the given position'''
        if self.is_empty():
            raise ValueError("The list is empty")
        if n > self.size:
            raise IndexError("Index greater than the size itself")
        newest = self._Node(e, None, None)
        predecessor = self.__find__(n)
        successor = predecessor.next
        newest.prev = predecessor
        newest.next = successor
        predecessor.next = newest
        successor.prev = newest
        self.size += 1

    def printlist(self):
        '''Prints the underlying circular linked list'''
        if self.is_empty():
            raise Exception("The list is empty")
        temp = self.header.next

        #NOTE: Here "is not" is being used instead of just "not". It is because "not" is a logical operator and it is used to negate a boolean expression. While "is not" is an identity operator, and it is used to check if two items do not have same identity (i.e, they are different objects in memroy)
        # while temp not self.trailer:

        while temp is not self.trailer:
            print(temp.element)
            temp = temp.next

# c = Circular_list()
# for i in range(10):
#     c.add(i)
# print(f"The lenght of the on=bject is {len(c)} \n")
# print("The list:")
# c.printlist()
# print("Inserting element in between, when the index is within boundaries")
# c.insert(12,3)
# print(f"The new lenghth of the object is {len(c)} \n")
# print("The new list:")
# c.printlist()
# print("Inserting element in between, when the index is not within boundaries")
# c.insert(12, 44)
