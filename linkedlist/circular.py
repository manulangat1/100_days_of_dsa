# all the nodes have value and ref to the next node
# the last node has ref to the  first node


class Node:
    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def insert(self, location, value):
        newNode = Node(value)
        if location == 0:
            if self.head is None:
                newNode.next = newNode
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode

        elif location == -1:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            print(tempNode)
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode

    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def search(self, searchValue):
        if self.head is None:
            return "Empty CLL"
        node = self.head
        while node:
            if node.value == searchValue:
                return f"found {node.value}"
            node = node.next

            if node == self.tail.next:
                break
        return "Not found"

    def delete(self, location):
        if location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                nextNode = self.head.next
                self.head = nextNode
                self.tail.next = nextNode
        elif location == -1:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node:
                    if node.next == self.tail:
                        break
                node.next = self.head
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                node = node.next
                if node == self.tail.next:
                    break
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next


myCLL = CircularLinkedList()
print([i.value for i in myCLL])
myCLL.create(5)
print([i.value for i in myCLL])
myCLL.insert(-1, 10)
print([i.value for i in myCLL])

myCLL.insert(1, 10)
print([i.value for i in myCLL])

print(myCLL.traverse())


print(myCLL.search(10))
# print([i.value for i in myCLL])

myCLL.delete(0)
print([i.value for i in myCLL])

myCLL.delete(-1)
print([i.value for i in myCLL])
