# Give an algorithm for finding the second to last node in a singly linked list in which the last node is indicatd by a next refrence to none

class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def SecondToLast(self):
        temp = self.head
        sec = None
        while temp.next is not None:
            sec = temp
            temp = temp.next
        return sec.val

    def PrintList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

if __name__ == "__main__":
    l1 = LinkedList()
    l1.head = Node(9)
    second = Node(8)
    third = Node(7)
    fourth = Node(6)
    fifth = Node(5)
    sixth = Node(4)
    seventh = Node(3)
    l1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    print("This is the linked list itself:")
    l1.PrintList()
    print(f"This is the value of second to last node -> {l1.SecondToLast()}")
