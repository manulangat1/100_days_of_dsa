from random import randint


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

            # if node == self.tail.next:
            #     break

    def __str__(self) -> str:
        values = [str(i.value) for i in self]
        return "--->".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            node = node.next
            result += 1
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head, self.tail = None, None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


customLL = LinkedList()

customLL.generate(10, 0, 99)

print(customLL)

print(len(customLL))
