### each node  has value and ref to the prev and next  nodes in the list. and allows for back and front traversal.


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DoublyLL:
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

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node

    def insertion(self, value, location):
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
        elif location == -1:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            # print(tempNode.value, index, location)
            nextNode = tempNode.next
            newNode.next = nextNode
            newNode.prev = tempNode
            nextNode.prev = newNode
            tempNode.next = newNode

    def traversal(self):
        if not self.head:
            return "Empty head value"
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def reverseTraversal(self):
        if not self.head:
            return "No head found"
        node = self.tail

        while node:
            print(node.value)
            node = node.prev

    def search(self, value):
        node = self.head

        while node:
            if node.value == value:
                return f"Found at {node.value}"
            node = node.next
        return "Not found"

    def deletion(self, location):
        if location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                nextNode = self.head.next
                nextNode.prev = None
                self.head = nextNode
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.head.next = None
            else:
                prevNode = self.tail.prev
                prevNode.next = None
                self.tail = prevNode
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 0
            tempNode.next = tempNode.next.next
            tempNode.next.prev = tempNode


myDLL = DoublyLL()
print([i.value for i in myDLL])
myDLL.createDLL(8)
print([i.value for i in myDLL])

myDLL.insertion(4, 0)
print([i.value for i in myDLL])

myDLL.insertion(4, -1)
print([i.value for i in myDLL])

myDLL.insertion(40, 1)
print([i.value for i in myDLL])

myDLL.traversal()
print()
myDLL.reverseTraversal()

print(myDLL.search(4))


myDLL.deletion(0)
print([i.value for i in myDLL])

myDLL.deletion(-1)
print([i.value for i in myDLL])

myDLL.deletion(0)
print([i.value for i in myDLL])
