# Write a program to delete an node in doubly linked list containing the value entered by the user.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.trail = None
        self.size = 0

    def __len__(self):
        return self.size

    def deleteNodeByValue(self,e):
        '''Delete The Node based on the value entered by the user'''
        temp = self.head.val
        while temp is not e:
            temp = temp.next.val
        predecessor = temp.prev
        successor = temp.next
        predecessor.next = successor
        successor.prev = predecessor
        temp = None
        self.size -= 1

    def printList(self):
        temp = self.head
        while temp.next is not None:
            print(temp.val)
            temp = temp.next

if __name__ == "__main__":
    l1 = DoublyLinkedList()
    l1.head = Node(9)
    l1.size +=1
    second = Node(8)
    l1.size +=1
    third = Node(7)
    l1.size +=1
    l1.head.next = second
    second.prev = l1.head
    second.next = third
    third.prev = second

    print(len(l1))
    l1.printList()
    l1.deleteNodeByValue(8)
    print(len(l1))
    l1.printList()
