# Describe in detail how to swap two nodes (x and y), (not just their contents) in a signly linked list. Only refrences of x and y are given. Also describe the same case for doubly linked list. Exxplain the time and space complexity for the program

class SinglyLinkedList:
    class Node:
        def __init__(self,val, nex):
            self.val = val 
            self.next = nex
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def append(self, e):
        newest = self.Node(e, None)
        # We are apending to the head of the linked list
        newest.next = self.head
        self.head = newest
        self.size += 1

    def dele(self):
        # we are deleting from the first node
        first_node = self.head.next
        element = self.head.val
        self.head.val = self.head.next = None
        self.head = first_node
        self.size -= 1
        return element


if __name__ == "__main__":
    l1 = SinglyLinkedList()
    print(f"The length of l1 before any addition is -> {len(l1)}")
    print("And the list itself is:")
    l1.printList()
    l1.append(9)
    l1.append(3)
    l1.append(7)
    l1.append(4)
    print(f"The length of l1 after appending at the front is -> {len(l1)}")
    print("And the list itself is:")
    l1.printList()
    print("The items in the list were shown in revrese order of appending. This is because we are appending the values on the front and the printList() method prints the values from first to last.")
