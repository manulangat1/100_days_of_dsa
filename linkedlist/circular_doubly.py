# each node has value , next , prev values
# Last node is linked to the first


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DCL:
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

    def createCDLL(self, value):
        newNode = Node(value)
        newNode.next = newNode
        newNode.prev = newNode

        self.head = newNode
        self.tail = newNode

    def insertion(self, value, location):
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        elif location == -1:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode


myDCL = DCL()
print([i.value for i in myDCL])
myDCL.createCDLL(8)
print([i.value for i in myDCL])

myDCL.insertion(5, 0)
print([i.value for i in myDCL])

myDCL.insertion(7, -1)
print([i.value for i in myDCL])
