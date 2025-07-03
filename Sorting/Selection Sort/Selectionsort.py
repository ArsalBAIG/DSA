def selection_sort(list1):
    n = len(list1)
    for i in range(n):
        min_index = i # Initally the i value is 0.
        for j in range(i + 1, n): # Here, we compare the 0th index with his next indexes.
            if list1[j] < list1[min_index]: #If we found that value at 0 index is greater than value at next indexes then.
                min_index = j
        list1[i], list1[min_index] = list1[min_index], list1[i] # Swapping element.

mylist = [34, 2, 78, 39, 93, 12]
selection_sort(mylist)
print(mylist)