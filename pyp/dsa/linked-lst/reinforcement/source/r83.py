# Develop a program to concatenate two sorted linked list L and M. Find the time complexity of your program.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def printList(self):
        temp = self.head 
        while temp is not None:
            print(temp.val)
            temp = temp.next

# How to sort a linked list
# Start with the head:
# check its values -> compare its values -> swap after comparing

    def sorte(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            if temp is not None and curr.val > temp.val:
                curr.val, temp.val = temp.val, curr.val
            prev = curr
            curr = temp 
            # temp = temp.next

    def concatenate(self, other):
        pass

if __name__ == "__main__":
    l1 = LinkedList()
    l1.head = Node(9)
    second = Node(8)
    third = Node(6)
    fourth = Node(7)
    l1.head.next = second
    second.next = third
    third.next = fourth
    print("This is the nornal list:")
    l1.printList()
    l1.sorte()
    print("This is the sorted list:")
    l1.printList()

