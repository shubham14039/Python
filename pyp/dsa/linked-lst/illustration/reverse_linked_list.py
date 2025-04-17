# Reverse a linked list such that the space complexity does not increase.
#

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        curr = self.head #This will store the starting point of the linked list
        while curr is not None:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp
        self.head = previous #NOTE: Not used until the loop is finished (Until the linked list is reversed). That means the last element is being set to the new self.head.

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

if __name__ == '__main__':
    l1 = LinkedList()
    l1.head = Node(9)
    second = Node(8)
    l1.head.next = second
    third = Node(5)
    second.next = third
    fourth = Node(7)
    third.next = fourth
    print("This is the original linked list")
    l1.printList()
    l1.reverse()
    print("This is the revrsed linked list")
    l1.printList()




