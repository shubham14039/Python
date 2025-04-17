# Give a complete implementation of stack ADT using a singly linked list that includes a header sntinel


class LinkedQueue:
    class _Node:
        def __init__(self, element, n):
            self.element = element
            self.next = n

    def __init__(self):
        self.head = self._Node(None, None)
        self.size = 0

    def __len__(self):
        "Returns the length of the queue"
        return self.size

    def is_empty(self):
        return self.size == 0

    def enque(self, e):
        '''Adds a new element at the back the queue'''
        newest = self._Node(e, None)
        last_node = self.__last()
        last_node.next = newest
        self.size += 1

    def deque(self):
        '''Removes and returns the first element from the list'''
        if self.is_empty():
            raise ValueError("The queue is empty")
        item = self.head.next
        ans = item.element
        temp = item.next
        self.head.next = temp
        item.element = item.next = None
        self.size -= 1
        return ans

    def peek(self):
        '''Checks the top element from the queue'''
        if self.is_empty():
            raise ValueError("The queue is empty")
        top = self.head.next
        return top.element

    def __last(self):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp
    
    def concatenate(self, other):
        '''Concatenates two LinkedQueue objects in one and deletes all the items from the second quueue'''
        if len(other) < 1:
            raise Exception(f"The {other} queue is empty")
        last = self.__last()
        other_first = other.head.next
        last.next = other_first
        other.head.next = None
        return self

    def printqueue(self):
        '''Prints the queue'''
        if self.is_empty():
            print("The Stack is epmty")
            return 
        temp = self.head.next
        while temp is not None:
            print(temp.element)
            temp = temp.next

Q = LinkedQueue()
R = LinkedQueue()
for i in range(10):
    Q.enque(i)
for i in range(11, 20):
    R.enque(i)
print("The queue Q:")
Q.printqueue()
print("The queue R:")
R.printqueue()
print("Concatenating both queues:")
Q.concatenate(R)
print("Final queue Q:")
Q.printqueue()
print("The queue R:")
R.printqueue()
