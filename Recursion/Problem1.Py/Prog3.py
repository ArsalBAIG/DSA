# Write a recursive function to print first N Odd natural numbers.

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')

def printNOdd(n):
    if n > 0:
        printNOdd(n - 1)
        print(2 * n - 1, end=' ') # This line, is actually printing frist 10 odd no accoriding to given no in the print(10) statement.
printNOdd(10)