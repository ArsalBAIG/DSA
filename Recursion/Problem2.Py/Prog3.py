# Write a recursive function to get the sum of first N Even numbers.

def SumNEven(n):
    if n == 1:
        return 2 # Bcz very first even no is 2 not 1.
    return 2 * n + SumNEven(n - 1)
# Here, 2 * n is the nth even number.

print("Even no is: ", SumNEven(10))