# Develop a program to find the middle of the linked list, by link hopping.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def oneMiddle(self):
        '''Find the middle node of the linked list'''
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next

        n = self.head
        for _ in range(count//2):
            n = n.next
        return n.val
    
    def anotherMiddle(self):
        '''Another way of finding the middle element'''
        temp1 = self.head
        temp2 = self.head
        while (temp1.next != None and temp1.next.next != None):
            temp1 = temp1.next.next
            temp2 = temp2.next
        return temp2.val


if __name__ == "__main__":
    l1 = LinkedList()
    l1.head = Node(9)
    second = Node(8)
    third = Node(7)
    fourth = Node(6)
    fifth = Node(5)
    sixth = Node(4)
    seventh = Node(3)
    eighth = Node(2)
    l1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eighth

    print(l1.oneMiddle())
    print(l1.anotherMiddle())
