# write a recursive function to print first N natural numbers in reverse order.

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')

def printNrev(n):
    if n > 0:
        print(n, end=' ')
        printNrev(n - 1)
printNrev(12)