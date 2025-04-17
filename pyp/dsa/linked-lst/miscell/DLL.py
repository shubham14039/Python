#NOTE: Write a function to reverse the linked list.
class _DoublyLinkedBase:
    '''
    A base class which stores the method objects that can be performed on the data object instances.
    '''
    class _Node:
        '''
        Light weight node class
        '''
        __slots__ = "_element", "_prev", "_next"
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0 

    def __len__(self):
        '''
        Returns the length of the data instance.
        '''
        return self._size

    def is_empty(self):
        '''
        Checks if the data instance is empty.
        '''
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''
        Inserts the element in between the predecessor and successor nodes.
        '''
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        #FIXME: Check for the problems
        return newest


    def _delete_node(self, node):
        '''
        Removes a node from the linked list.
        '''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._next = node._prev = node._element = None
        return element

    def reverse(self):
        prev = None
        curr = self._header
        while curr is not None:
            temp = curr._next
            curr._next = prev
            prev = curr
            curr = temp
        self._header = prev
        return self #returning self helps in method chaining, that means -> we can chain other methods with this method.

    def printList(self):
        temp = self._header
        while temp  is not None:
            print(temp._element)
            temp = temp._next

class DoublyLinkedStack(_DoublyLinkedBase):
    '''
    A Doubly linked list instance for Stack operations.
    '''

    def top(self):
        '''
        Returns the top element of the stack.
        '''
        if self.is_empty():
            return "Empty: The Stack is empty"
        return self._header._next._element

    def push(self,e):
        '''
        Appends a new element in the stack.
        '''
        self._insert_between(e, self._header , self._header._next)

    def pop(self):
        '''
        Removes an element from the stack instance.
        '''
        self._delete_node(self._header._next)

    def reverseStack(self):
        self.reverse()

    def printStack(self):
        self.printList()


l1 = DoublyLinkedStack()
l1.push(9)
l1.push(8)
l1.push(7)
l1.push(6)
l1.push(5)
print("This is the original stack")
l1.printStack()
print("This is the reversed stack")
l1.reverseStack()
l1.printStack()

#FIXME: Not working properly

class DoublyLinkedQueue(_DoublyLinkedBase):
    '''
    A Doubly linked list instance for queue operations.
    '''

    def first(self):
        '''
        Returns the first element of the queue instance.
        '''
        if self.is_empty():
            return "Empty: The queue is empty"
        return self._header._next._element

    def enque(self, e):
        '''
        Adds a new element at the end of the end of the queue.
        '''
        self._insert_between(e, self._trailer._prev, self._trailer)

    def deque(self):
        '''
        Removes and returns the first element from the queue.
        '''
        self._delete_node(self._header._next)


class DoublyLinkedDEQueue(_DoublyLinkedBase):
    '''
    A doubly linked list instance for doubly ended queue.
    '''

    def first(self):
        '''
        Returns the first element from the DEque.
        '''
        if self.is_empty():
            return "Empty: The DEqueue is empty"
        return self._header._next._element

    def last(self):
        '''
        Returns the last element from the DEque.
        '''
        if self.is_empty():
            return "Empty: The DEqueue is empty"
        return self._trailer._prev._element

    def add_first(self, e):
        '''
        Adds a new element on the front of the DEque.
        '''
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''
        Adds a new element on the end of the DEque.
        '''
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        '''
        Removes and returns the first element from the DEque.
        '''
        if self.is_empty():
            return "Empty: The DEqueue is empty"
        self._delete_node(self._header._next)

    def delete_last(self):
        '''
        Removes and returns the last element from the DEque.
        '''
        if self.is_empty():
            return "Empty: The DEqueue is empty"
        self._delete_node(self._trailer._prev)


#TODO: Testing of functions


#TEST: Test for stack 
stack = DoublyLinkedStack()

# Test pushing elements
stack.push(1)
stack.push(2)
stack.push(3)

# Test peeking the top element
print("Peek (expected: 3):", stack.top())  # Expected: 3

# Test popping elements
#FIX: Not working
print("Pop (expected: 3):", stack.pop())  # Expected: 3

# Test if stack is empty
print("Is stack empty? (expected: False):", stack.is_empty())  # Expected: False

# Test the size of the stack
print("Stack size (expected: 2):", len(stack))  # Expected: 2
print("Testing of stack STAGE 01 finished\n")


#TEST: Test for queue 
queue = DoublyLinkedQueue()

# Test enqueuing elements
queue.enque(10)
queue.enque(20)
queue.enque(30)

# Test front element
print("Front (expected: 10):", queue.first())  # Expected: 10

# Test dequeuing elements
#FIX: Not working
print("Dequeue (expected: 10):", queue.deque())  # Expected: 10

# Test if queue is empty
print("Is queue empty? (expected: False):", queue.is_empty())  # Expected: False

# Test the size of the queue
print("Queue size (expected: 2):", len(queue))  # Expected: 2
print("Testing of queue STAGE 01 finished\n")


#TEST: Test for DEqueue 
deque_instance = DoublyLinkedDEQueue()

# Test appending elements to the right
deque_instance.add_last(5)
deque_instance.add_last(10)

# Test appending elements to the left
deque_instance.add_first(15)

# Test popping elements from the right
#FIX: Not working
print("Pop right (expected: 10):", deque_instance.delete_last())  # Expected: 10

# Test popping elements from the left
#FIX: Not working
print("Pop left (expected: 15):", deque_instance.delete_first())  # Expected: 15

# Test peeking front and rear elements
print("Peek front (expected: 5):", deque_instance.first())  # Expected: 5
print("Peek rear (expected: 5):", deque_instance.last())  # Expected: 5

# Test if deque is empty
print("Is deque empty? (expected: False):", deque_instance.is_empty())  # Expected: False

# Test the size of the deque
print("Deque size:", len(deque_instance))
print("testing of dequeue STAGE 01 finished\n")

print("testing of STAGE 01 finished\n")


#TODO: Testing of functions (some harder methods)

#TEST: Test for stacks 
stack = DoublyLinkedStack()

# Test large number of pushes
for i in range(1000):
    stack.push(i)
print("Stack size after 1000 pushes (expected: 1000):", len(stack))  # Expected: 1000

# Test interleaved push and pop
stack.push(1001)

#FIX: Not working
print("Pop after push (expected: 1001):", stack.pop())  # Expected: 1001

print("Peek after pop (expected: 999):", stack.top())  # Expected: 999 

# Test popping all elements
while not stack.is_empty():
    stack.pop()
print("Stack size after popping all elements (expected: 0):", len(stack))  # Expected: 0

# Test pop on empty stack
#FIX: Not working
print("Pop on empty stack (expected: Stack is epmty):", stack.pop())  # Expected: "Stack is empty"
print("TEST ON STACK COMPLETED SUCESSFULLY\n")


#TEST: Test for queues:
queue = DoublyLinkedQueue()

# Test large number of enqueues
for i in range(1000):
    queue.enque(i)
print("Queue size after 1000 enqueues:", len(queue))

# Test interleaved enqueue and dequeue
queue.enque(1001)

#FIX: Not working
print("Dequeue after enqueue (expected; 0):", queue.deque())  # Expected: 0

print("Front after dequeue (expected: 1):", queue.first())  # Expected: 1

# Test dequeuing all elements
while not queue.is_empty():
    queue.deque()
print("Queue size after dequeuing all elements (expected: 0):", len(queue))  # Expected: 0

# Test dequeue on empty queue
#FIX: Not working
print("Dequeue on empty queue (expected: Queus is empty):", queue.deque())  # Expected: "Queue is empty"
print("TEST ON QUEUE COMPLETED SUCESSFULLY\n")


#TEST: test for double ended queues 
deque_instance = DoublyLinkedDEQueue()

# Test large number of appends and appendlefts
for i in range(500):
    deque_instance.add_last(i)
    deque_instance.add_first(i + 1000)
print("Deque size after appends and appendlefts:", len(deque_instance))

# Test interleaved pops from both ends
#FIX: Not workng 
print("Pop right after appendlefts (expected: 499):", deque_instance.delete_last())  # Expected: 499

#FIX: Not working
print("Pop left after appends (expected: 1499):", deque_instance.delete_first())  # Expected: 1499

# Test dequeuing all elements
while not deque_instance.is_empty():
    deque_instance.delete_last()
print("Deque size after popping all elements (expected: 0):", len(deque_instance))  # Expected: 0

# Test pop on empty deque
#FIX: Not working
print("Pop on empty deque (expected: deque is empty):", deque_instance.delete_last())  # Expected: "Deque is empty"
print("TEST ON DEQUEUE COMPLETED SUCESSFULLY")
