# Given the instances to the first elements of two singly linked lists, write a program to concatenate two singly linked lists.

class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    #FIXME: While this concatenation might work, it has some issues with handling the edge cases. Like when either of the tow lists are empty.
    def concatenate(self, other):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = other.head

if __name__ == "__main__":
    l1 = LinkedList()
    l1.head = Node(1)
    second = Node(9)
    third = Node(8)
    fourth = Node(7)
    l1.head.next = second
    second.next = third
    third.next = fourth
    print("This is the first list")
    l1.printList()
    l2 = LinkedList()
    l2.head = Node(2)
    two = Node(3)
    three = Node(4)
    l2.head.next = two
    two.next = three
    print("This is the second list")
    l2.printList()
    print("This is the concatenated list:")
    l1.concatenate(l2)
    l1.printList()
    
