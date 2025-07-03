# Quadratic Complexity.

def quadratic_algo(items):
    for i in items:
        for j in items:
            print(items, " ", items)

quadratic_algo([7,6,5,4])

# Here, the algorithm done:

# 1- outer loop iterates all the items. 
# 2- inner loop iterates all the items again.
# 3- total no of steps are n*n.