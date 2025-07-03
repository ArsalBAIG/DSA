# Write a recursive function to print first N Even natural numbers in reverse order.

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')

def printNEvenRev(n):
    if n > 0:
        print(2 * n, end=' ')
        printNEvenRev(n - 1)
printNEvenRev(10)