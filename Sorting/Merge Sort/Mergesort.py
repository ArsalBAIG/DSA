def MergeSort(list1):
    if len(list1) > 1:
        mid_index = len(list1) // 2
    # In below we're break list into two lists. 
        leftList = list1[ : mid_index]
        rightList = list1[mid_index: ]
    # This will apply when list contain only one element so the only one element in the list as it is divided into two list will be printed.
        MergeSort(leftList)
        MergeSort(rightList)

        i, j, k = 0, 0, 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                list1[k] = leftList[i]
                i += 1
            else:
                list1[k] = rightList[j]
                j += 1
            k += 1
    # This loop is done when the elements of the any sublist ends then this conditions continue.
        while i < len(leftList):
            list1[k] = leftList[i]
            i += 1
            k += 1
        while j < len(rightList):
            list1[k] = rightList[j]
            j += 1
            k += 1
mylist = [23, 45, 66, 89, 12, 32, 98, 23, 91, 22, 88, 54]
MergeSort(mylist)
print(mylist)