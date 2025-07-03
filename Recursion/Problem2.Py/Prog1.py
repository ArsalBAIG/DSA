# Write a recursive function to get the sum of first N natural numbers.

def SumN(n):
    if n == 1:
        return 1
    return n + SumN(n - 1)
print(f"Sum is: {SumN(10)}")
