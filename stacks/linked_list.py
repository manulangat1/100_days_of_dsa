class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head

        while currNode:
            yield currNode
            currNode = currNode.next


class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(x.value) for x in self.LinkedList]
        print(values)
        return "--->".join(values)

    def is_empty(self):
        if self.LinkedList.head is None:
            return True
        return False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def pop(self):
        self.LinkedList.head = self.LinkedList.head.next

    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


myStack = Stack()

print(myStack.is_empty())

print(myStack.push(34))
print(myStack.push(58))

print(myStack.is_empty())

print(myStack)
myStack.push(1000)

myStack.pop()

print(myStack)


print(myStack.peek(), "--->")

myStack.delete()

print(myStack)
