# write code to remove duplicates in an unsorted linked list
#  iterate and add to a set the duplicate and remove it
#  check the next node whether it is on the  set if yes remove it if no add it to the set

from questions import LinkedList


# with temp buffer


def removeDuplicates(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])

        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
    return ll


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print("----")
print(removeDuplicates(customLL))


def removeDuplicatesWithNoBuffer(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
    return ll


print("----")
print(removeDuplicatesWithNoBuffer(customLL))
