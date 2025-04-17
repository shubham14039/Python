# Implement a program transfer(S,T) that transfers all elements from S to T such that element on the top() of S gets pushed first into T



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


def transfer(S: ArrayStack, T: ArrayStack) -> ArrayStack:
    for _ in range(len(S)):
        T.push(S.pop())
    return T

k = ArrayStack()
j = ArrayStack()

for i in range(20):
    k.push(i)

print(transfer(k,j))

