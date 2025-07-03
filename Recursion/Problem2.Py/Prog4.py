# Write a recursive function to calculate factorial of numbers.

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
print("Factorial is: ", fact(5))