# Write a program to reverse a linked list

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseList(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next


#This is an imlementation of reversing a doubly linked list usign the same method above

class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reverseList(self):
        # previous  = Node(None)
        previous  = None
        current = self.head
        while current is not None:
            temp  = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

if __name__ == '__main__':
    l1 = DoublyLinkedList()
    l1.head = Node(9)
    second = Node(8)
    third = Node(4)
    fourth = Node(3)
    l1.head.next = second
    l1.head.prev = None
    second.next = third
    second.prev = l1.head
    third.next = fourth
    third.prev = second
    fourth.prev = third
    fourth.next = None
    print("This is the original list:")
    l1.printList()
    l1.reverseList()
    print("This is the modified list:")
    l1.printList()

