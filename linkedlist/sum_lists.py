"""
2 numbers represented by LL where each node contains a single value / digit. 
The digits are stored in reverse order such that the 1's digit  repre the head of the list. 
Write a fn that adds the two numbers and returns the sum as a LL
"""

from questions import LinkedList


def sumOfList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    curry = 0
    ll = LinkedList()

    while n1 or n2:
        result = curry
        if n1:
            result += n1.value
            print(result, n1.value)
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        print("my result", result)
        ll.add(int(result % 10))
        curry = result / 10
    print(curry, "f")
    return ll


customLL = LinkedList()
customLL.generate(10, 0, 99)

customLL1 = LinkedList()
customLL1.generate(10, 0, 99)

print(customLL, customLL1)
print("----")
print(sumOfList(customLL, customLL1))
