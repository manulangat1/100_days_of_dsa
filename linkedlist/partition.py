# write code to partiton a linked list around a value x , such that all values less than x come before x and the values more than or equal to x come after it


from questions import LinkedList


def partiton(ll, x):
    print("here")
    currNode = ll.head
    ll.tail = currNode

    while currNode:
        nextNode = currNode.next
        currNode.next = None

        if currNode.value < x:
            currNode.next == ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:
        ll.tail.next = None
    # return ll


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print("---")
print(partiton(customLL, 40))
