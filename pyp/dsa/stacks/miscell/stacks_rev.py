
#TODO: This is the implementation of the stacks again

# properties of stacks:
# 1. push 
# 2. pop
# 3. chekc of emptiness
# 4. return the last appended item 
# 5. LIFO principle 

class ArrayStacks:
    def __init__(self):
        self._data = []
        # self._size = 0

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == 0 

    def pop(self):
        if self.is_empty():
            raise Exception("Empty: Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            rase Exception("Empty: The Stack is empty")
        return self._data[-1]

    def push(self, e):
        self._data.append(e)


