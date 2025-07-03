# Write a recursive function to get the sum of first N Odd numbers.

def SumNOdd(n):
    if n == 1:
        return 1
    return 2* n-1 + SumNOdd(n - 1) 
# Here, 2 * n - 1 is the nth odd number.

print("Odd number is: ", SumNOdd(10))