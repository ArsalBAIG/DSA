def insertion_sort(list1):
    n = len(list1)
    for i in range(1, n): # The value starts from 1 bcz 0 value is already sorted.
        temp = list1[i]

        j = i - 1 # It compares the current element i on left side with the highest element of sorted array on the left side.
        while j >= 0 and temp < list1[j]:
            list1[j + 1] = list1[j] # This lines pushes the j to the right side.
            j -= 1
        list1[j + 1] = temp

mylist = [33, 32, 45, 122, 78, 12]
insertion_sort(mylist)
print(mylist)
