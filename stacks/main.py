# Is a data structure that follows the LIFO method eg a pile of plates and the back button of a website.
# creation can be by using a list or a linked list.
# by lists can also be size limit or not
import random


class Stack:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def is_empty(self):
        return True if len(self.list) == 0 else False

    def peek(self):
        pass

    def push(self, value):
        # append to the first element
        return self.list.append(value)

    def pop(self):
        if self.is_empty():
            return "No eleme to pop"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "No eleme to pop"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


myStack = Stack()
print(myStack.is_empty())
myStack.push(5)
print(myStack)
print(myStack.pop())
print("--->")
print(myStack)
for i in range(5):
    myStack.push(random.randint(i, 100))
print(myStack)

print("--->")
print(myStack.peek())
