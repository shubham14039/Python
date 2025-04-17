
class ArrayStack:
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
            return "Empty:The stack is empty"
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            return "Empty:The stack is already empty"
        return self._data.pop()


# Check for delimiters using stacks:

def delim(data):
    lefty = '({['
    righty = ')}]'

    S = ArrayStack()
    for i in data:
        if i in lefty:
            S.push(i)
        elif i in righty:
            if S.is_empty():
                return False
            elif righty.index(i) != lefty.index(S.pop()):
                return False
    return True
# data = "[{()}]"
# data = "[[]{([])}()]"
# data = "{}[(])]"
# print(delim(data))
