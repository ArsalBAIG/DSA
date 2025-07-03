# Write a recursive function to calculate sum of square of first N natural numbers.

def SqrN(n):
    if n == 1:
        return 1
    return n * n + SqrN(n - 1)
print('Sum of Square is: ', SqrN(5))