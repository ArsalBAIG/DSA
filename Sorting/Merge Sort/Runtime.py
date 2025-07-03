def Merge_Sort(array):
    if len(array) > 1:
        mid_index = len(array) // 2
        leftArray = array[ : mid_index]
        rightArray = array[mid_index: ]
        Merge_Sort(leftArray)
        Merge_Sort(rightArray)
        i, j, k = 0, 0, 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
                k += 1
        while i < len(leftArray):
            array[k] = array[i]
            i += 1
            k += 1
        while j < len(rightArray):
            array[k] = array[j]
            j += 1
            k += 1
            