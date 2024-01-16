import random


class Stack:
    def __init__(self, value=None) -> None:
        self.list = []
        self.maxSize = value

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "->".join(values)

    def is_empty(self):
        return True if len(self.list) == 0 else False

    def is_full(self):
        if len(self.list) == self.maxSize:
            return True
        return False

    def push(self, value):
        if self.is_full():
            return "Full stack"
        return self.list.append(value)

    def pop(self):
        if self.is_empty():
            return "Empty"
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.list[len(self.list) - 1]


myStack = Stack(6)
print(myStack)
for i in range(5):
    myStack.push(random.randint(i, 100))

print(myStack)

print(myStack.push(200))
print(myStack)

print(myStack.peek())
print(myStack)

print(myStack.pop())
print(myStack)
