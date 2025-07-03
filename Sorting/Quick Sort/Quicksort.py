# Here, lesser is the left sub-list & greater is the right sub-list.

import random
def Quick_Sort(listi):
    if len(listi) <= 1:
        return listi
    else:
        pivot_index = random.randint(0, len(listi) - 1) # pivot element is generally 0th index element.
        pivot = listi[pivot_index]
        lesser = [x for x in listi[0: ] if x < pivot] # First x is used to store the value of second x which is generally the x for the loop.
        greater = [x for x in listi[0: ] if x > pivot]
        return Quick_Sort(lesser) + [pivot] + Quick_Sort(greater) # Recursively call Quick_Sort func.

mylist = [23, 8, 3, 12, 45, 65, 34, 89, 32]
sorted_list = Quick_Sort(mylist)
print(sorted_list)