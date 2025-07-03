def Modified_BubbleSort(array):
    swapped = False
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) -i -1): # It ensure the inner loop doesn't iterate over the already sorted elements.
            if array[j] > array[j + 1]: #It checks, if current element is greater than next element.
                temp = array[j]
                array[j] = array[j + 1] # It assign the next element value to current element.
                array[j + 1] = temp
                swapped = True
        if not swapped:
            break

data = [-5, 45, 78, 0, 12, 25]
Modified_BubbleSort(data)
print("Sorted Array is: ", data)