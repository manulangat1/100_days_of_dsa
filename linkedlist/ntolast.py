# remove element n to last
# have 2 pointers with n distance between them . When the last reaches the tail / end then the first will be n places from the end.
from questions import LinkedList


def nToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print("---")
print(nToLast(customLL, 5))
