# SLL


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def insert(self, value, position):
        # at the beginning
        # at the middle
        # at the end
        if position == 0:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        elif position == -1:
            newNode = Node(value)
            # newNode.next = Node
            self.tail.next = newNode
            self.tail = newNode
        else:
            curr = 0
            node = self.head
            newNode = Node(value)
            while curr < position - 1:
                node = node.next
                curr += 1
            print(curr, position - 1)
            nextNode = node.next
            node.next = newNode
            newNode.next = nextNode

    # traversal

    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    # search

    def search(self, searchItem):
        if not self.head:
            return " Cannot search an empty list"

        node = self.head
        while node:
            if node.value == searchItem:
                return "Found at"
            node = node.next
        return "Not found"

    # delete node

    def delete(self, location):
        if self.head is None:
            return "Cannot delete does not exist "

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node

        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            tempNode.next = tempNode.next.next


mySLL = SLL()
node1 = Node(1)
node2 = Node(2)

mySLL.head = node1
mySLL.head.next = node2
mySLL.tail = node2

mySLL.insert(3, 0)

print(mySLL)

print([i.value for i in mySLL])

mySLL.insert(4, -1)
print([i.value for i in mySLL])

mySLL.insert(4, 1)
print([i.value for i in mySLL])


mySLL.traverse()

print(mySLL.search(1))

print([i.value for i in mySLL])
mySLL.delete(0)
print([i.value for i in mySLL])

mySLL.delete(-1)
print([i.value for i in mySLL])

mySLL.delete(1)
print([i.value for i in mySLL])
