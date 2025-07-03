import random
def Quick_Sort(Array):
    if len(Array) <= 1:
        return Array
    else:
        pivot_index = random.randint(0, len(Array) - 1)
        pivot = Array[pivot_index]
        lesser = [x for x in Array[0: ] if x < pivot]
        greater = [x for x in Array[0: ] if x > pivot]
        return Quick_Sort(lesser) + [pivot] + Quick_Sort(greater)

myArray = [23, 45, 2, 55, 93, 21]
sorted_Array = Quick_Sort(myArray)
print(sorted_Array)