# Write a recursive function to print first N Odd natural numbers in reverse order.

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')

def printNOddRev(n):
    if n > 0:
        print(2 * n-1, end=' ')
        printNOddRev(n - 1)
printNOddRev(10)