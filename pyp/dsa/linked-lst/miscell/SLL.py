# NOTE: Write a function to reverse the linked list.

# NOTE: Implementations of a singly linked lists in various scenarios

#  1. Implemantation of Singly linked list (for a stack)
class LinkedStack:
    class _Node:
        __slots__ = "element", "next"
        def __init__(self, element, nxt):
            self.element = element
            self.next  = nxt

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise ValueError("The Stack is empty")
        return self.head.element
    
    def pop(self):
        if self.is_empty():
            raise ValueError("The stack is empty")
        answer = self.head.element
        self.head = self.head.next
        self._size += 1
        return answer

    def push(self, e):
        self.head = self._Node(e, self.head)
        self._size += 1

    def reverseStack(self):
        '''This method reverses the linked list (Linked Stack) in place. Iterative method.'''
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def printList(self):
        '''Method for printing the contnts of the list iteratively'''
        temp = self.head
        while temp is not None:
            print(temp.element)
            temp = temp.next

l1 = LinkedStack()
l1.push(9)
l1.push(8)
l1.push(7)
l1.push(6)
l1.push(5)
print("This is the original list")
l1.printList()
l1.reverseStack()
print("This is the reverse list")
l1.printList()

# NOTE: Usage of __slots__ in the node instance:
#    This __slots__ attribute is used to allocate a fixed amount of memeory for attributes, rather than usage of dynamic dixtionary __dict__ which is automatically used while creation. Moreover, it helps in faster attribute acess, rather than lookups in the traditional __dict__. Also, it controls how many attribtes a class can have (internally), thus limiting the control from outside the class (encapsulation).

#  2. Implementation of a queue using a singly linked list

class LinkedQueue:
    class _Node:
        def __init__(self,element,nxt):
            self.element = element
            self.next = nxt
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError("The queue is empty")
        return self.head.elemnt

    def last(self):
        if self.is_empty():
            raise ValueError("The queue is empty")
        return self.tail.element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
            # self.tail = newest #In this case -> the tail is assigned only when there is no node.;
        self.tail = newest #in this case -> the tail is assigned ragrdless
        self._size += 1


    def dequeue(self):
        if self.is_empty():
            raise ValueError("The queue is empty")
        answer = self.head.element
        successor = self.head
        self.head = self.head.next
        #Deleting the previous head node. (It was in then memeory even after we assigned the next node as self.head)
        del successor
        self._size -= 1
        # If the list is empty after deleting the very last node, the self.tail node is removed from the memory. 
        if self.is_empty():
            self.tail.element = self.tail.next = self.tail = None
        return answer

 # Implementation of a double ended queue with Singly Linked list
class LinkedDeque:
    class _Node:
        __slots__ = "element", "next"
        def __init__(self, element, nxt):
            self.element = element
            self.next = nxt

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self.head.element

    def last(self):
        return self.tail.element

    def add_first(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            newest.next  = self.head
            self.head = newest
        self._size += 1
        #OTHER WAY OF DOING SAME THING:
        # This method does not care if there is no existing linked list. And if there is no any, then it assigns its next node to itself. This does not particularly follows the covention of last node pointing to none (in this case it will point to itself, when new nodes will be added)
        # self.head = self._Node(e, self.head)
        # self._size += 1

    def add_last(self,e):
        newest = self._Node(e, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest #When there is no existing node, then the tail should also point to the same new node.

        else:
            self.tail.next = newest
            self.tail = newest
        self._size += 1
    def remove_first(self):
        pass

    def remove_last(self):
        pass




class CircularQue:
 class _Node:
     __slots__ = "_element", "_next"
     def __init__(self, element, next):
         self._element = element
         self._next = next

 def __init__(self):
     self._tail = None
     self._size = 0

 def __len__(self):
     return self._size

 def is_empty(self):
     return self._size == 0

 def first(self):
     if self.is_empty():
         raise ValueError("The queue is empty")
     head = self._tail._next 
     return head._element

 def deque(self):
     if self.is_empty():
         raise ValueError("The queue is empty")
     oldhead = self._tail._next
     if self._size == 1:
         self._tail = None
     self._tail._next = oldhead._next
     self._size -= 1
     return oldhead._element

 def enque(self, e):
     newest = self._Node(e, None)
     if self.is_empty():
         newest._next = newest
     else:
         newest._next = self._tail._next
         self._tail._next = newest
     self._tail = newest
     self._size += 1

 def rotate(self):
     if self._size > 0:
         self._tail = self._tail._next



class CircularLinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Empty: The circular queue is empty")
        head = self._tail._next
        return head

    def enque(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest #FIX: Why newest is assigned as the tail onject
        self._size += 1

    def deque(self):
        if self.is_empty():
            raise Exception("Empty: The circular queue is empty")
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        self._tail._next = head._next
        self._size -= 1
        return head._element

    def rotate(self):
        '''
        Used for rotating the queue externally
        '''
        if self._size > 0:
            self._tail = self._tail._next

    def queue(self):
        current = self.first
        queue_elements = []
        while current:
            queue_elements.append(current._element)
            current = current._next
        return queue_elements

# Create a Queue instance
q = CircularLinkedQueue()

# Test 1: Enqueue elements
q.enque(10)
q.enque(20)
q.enque(30)
print("1. After enqueue operations:", q.queue)  # Expected: [10, 20, 30]

# Test 2: Dequeue an element
dequeued_element = q.deque()
print("2. Dequeued element:", dequeued_element)  # Expected: 10
print("3. Queue after dequeue operation:", q.queue)  # Expected: [20, 30]

# Test 3: Peek at the front element
front_element = q.first()
print("4. Front element:", front_element)  # Expected: 20

# Test 4: Check if the queue is empty
is_empty = q.is_empty()
print("5. Is the queue empty?", is_empty)  # Expected: False

# Test 5: Check the size of the queue
queue_size = len(q)
print("6. Queue size:", queue_size)  # Expected: 2

#OPTIMIZE: All enque operations working properly

#FIXME: deque not working properly

# Test 6: Dequeue all elements to make the queue empty
q.deque()
q.deque()
print("7. Queue after dequeuing all elements:", q.queue)  # Expected: []

# Test 7: Attempt to dequeue from an empty queue
dequeued_element_empty = q.deque()
print("8. Attempt to dequeue from empty queue:", dequeued_element_empty)  # Expected: "Queue is empty"

# Test 8: Check if the queue is empty after all dequeues
is_empty_after_all = q.is_empty()
print("9.Is the queue empty after all dequeues?", is_empty_after_all)  # Expected: True
