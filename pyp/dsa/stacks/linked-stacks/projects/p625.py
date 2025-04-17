# Suppose a string contains a random series of n X's and n Y's. X correspond to a push operation and Y correspond to a pop operation, and the stack is initially empty. Develop a python application to check whether a given string Str representing a sequence of X's and Y's is feasible in a stack or not.

# what it means:
#     1. At no point the operation Y (pop) occurs when the stack is empty
#     2. The number of X should be greater than the number of Y's.

class LinkedStack:
    class _Node:
        def __init__(self, element, nx):
            self.element = element
            self.next = nx

    def __init__(self):
        self.head = self._Node(None, None)
        self.size = 0 

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        newest = self._Node(e, None)
        successor = self.head.next
        newest.next = successor
        self.head.next = newest
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("The Stack is empty")
        current = self.head.next
        current_nxt = current.next
        self.head.next =current_nxt
        current.next = current.element = None
        self.size -= 1

if __name__ == "__main__":
    s = input("Input your string: ")
    try:
        ls = ["Y", "X"]
        for i in s:
            if i not in ls:
                raise KeyError()
        S = LinkedStack()
        for i in s:
            if i == "X":
                S.push(i)
            else:
                S.pop()
        print("Feasible")

    except ValueError:
        print("Not Feasible")
    except KeyError:
        print("String containing only X's and Y's allowed.")
    except:
        print("Invalid input")
