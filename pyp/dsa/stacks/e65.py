# Write a python program that reverses a string entered by the user using stacks

# Steps:
#     1. push all the characters in the stack
#     2. pop and add all the characters into a new string

# Let us first define a stack class using arrays:

class ArrayStacks:
    def __init__(self):
        self._data = []

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        return self._data.pop()

    def push(self, e):
       self._data.append(e)



def rev_str(data: str):
    S = ArrayStacks()
    for char in data:
        S.push(char)
###################################
    new_string = []
    while not S.is_empty():
        new_string.append(S.pop())
    return ''.join(new_string)
###################################
# Alternate code for the above:
    # reverse_string = ''
    # while S:
        # reverse_string += S.pop()
    # return reverse_string
# NOTE: both methods in the while loop have same time and space complexities. But the latter one is more pythonic and mitght perform well in large codebases

