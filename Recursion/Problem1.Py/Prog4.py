# Write a recursive function to print first N Even natural numbers.

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')

def printNEven(n):
    if n > 0:
        printNEven(n - 1)
        print(2 * n, end=' ') # This line, is actually printing frist 10 even no accoriding to given no in the print(10) statement.
printNEven(10)