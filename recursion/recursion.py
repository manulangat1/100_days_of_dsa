# way of solving a problem where the function calls itself.
## To write recursive functions. The following steps should be followed.
### 1. Have the recursiove flow.
### 2. Have the base condition.
### 3. Check need for a constraint and have it.


def factorial(n):
    # constraint
    assert n >= 0 and n == int(n), "The number should be a positive number only"
    # base condition
    if n in [0, 1]:
        return 1
    # your flow
    else:
        return n * factorial(n - 1)


print(factorial(40))


def fibonnace(n):
    assert n >= 0 and n == int(n), "The number should be a positive number only"

    if n in [0, 1]:
        return n
    else:
        return fibonnace(n - 1) + fibonnace(n - 2)


print(fibonnace(5))

# sum of digits


print()
print(" sum of digits ")


def sumOfDigits(n):
    print(n)
    assert n >= 0 and n == int(n), "The numbers should be positive numbers only"

    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))


print(sumOfDigits(98))


print()
print(" calculate power of a number using recursion")


def powerOfNumber(n, exp):
    assert exp >= 0 and int(exp) == exp, "The numbers should be positive only"
    if exp == 0:
        return 1
    if exp == 1:
        return n
    return n * powerOfNumber(n, exp - 1)


print(powerOfNumber(3, 40))

print()
print("find GCD")
"""
greatest positive number that divides all the numbers
"""


def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers should be int"
    if a < 0:
        return -1 * a
    if b < 0:
        return -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, b % a)


print(gcd(15, 3))


print()
print("decimal to binary")


def decimalToBinary(n):
    assert n >= 0 and int(n) == n, "The numbers should be positive only"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n / 2))


print(decimalToBinary(10))

### Big O is the metric to measure efficieny of an algorithm.


### find the biggest number
def biggestNumber(array, n):
    if n == 1:
        return array[0]
    else:
        return max(array[n - 1], biggestNumber(array, n - 1))


print(biggestNumber([1, 2, 3, 4], 4))
