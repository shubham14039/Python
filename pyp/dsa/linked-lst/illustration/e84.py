# Develop a program which concatenates two doubly linked lists (with header and trailer sentinels)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.header = Node(None)
        self.trailer = Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    #THIS WORKS BUT NOT THE INTENDED WAY
    # Cancatenation includes the header and trailer sentinels from the first and second linked lists
    def concatenate(self, other):
        self.trailer.next = other.header
        other.header.prev = self.trailer
        self.trailer = other.trailer
        

    def printList(self):
        temp = self.header.next
        while temp is not self.trailer:
            print(temp.val)
            temp = temp.next

if __name__ == "__main__":
    l1 = DoublyLinkedList()
    second = Node(9)
    third = Node(8)
    fourth = Node(7)
    l1.header.next = second
    second.prev = l1.header
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = l1.trailer

    print("This is the Doubly linked list")
    l1.printList()

    #SECOND LINKED LIST START
    l2 = DoublyLinkedList()
    two = Node(1)
    three = Node(2)
    four = Node(3)
    l2.header.next = two
    two.prev = l2.header
    two.next = three
    three.prev = two
    three.next = four
    four.prev = three
    four.next = l2.trailer
    print("This is the second list:")
    l2.printList()
    #CONCATENATE
    l1.concatenate(l2)
    print("And this is the concatenated list:")
    l1.printList()
