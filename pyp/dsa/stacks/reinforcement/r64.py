# Give a recursive method for removing all the items from a stack


class ArrayStack:

    def __init__(self) -> None:
        self._data = []

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        return self._data.pop()



def rec_rem(S: ArrayStack):
    pass
