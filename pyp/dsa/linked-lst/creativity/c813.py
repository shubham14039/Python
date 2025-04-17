# Give a complete implementation of stack ADT using a singly linked list that includes a header sntinel


class LinkedStack:
    class _Node:
        def __init__(self, element, n):
            self.element = element
            self.next = n

    def __init__(self):
        self.head = self._Node(None, None)
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        newest = self._Node(e, None)
        old_last = self.top()
        old_last.next = newest
        self.size += 1

    #NOTE: Here we are removing the last element in the stack because new elements are being added on the last. But if they were being added from the front, from the header, then we would have been removing the elements from the top
    def pop(self):
        if self.is_empty():
            raise ValueError("The Stack is empty")
        last_node = self.top()
        ans = last_node.element
        # How to remove the last element from a singly linked list
        self.size -= 1
        return ans

    def top(self):
        # if self.is_empty():
        #     raise ValueError("The stack is empty")
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp

    def printlist(self):
        if self.is_empty():
            print("The Stack is epmty")
            return 
        temp = self.head.next
        while temp.next is not None:
            print(temp.element)
            temp = temp.next



S = LinkedStack()
S.printlist()
for i in range(10):
    S.push(i)

S.printlist()
