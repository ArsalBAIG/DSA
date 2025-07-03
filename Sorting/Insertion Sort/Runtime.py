def Insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j + 1]= array[j]
            j -= 1
        array[j + 1] = temp

mydata = [34, 2, 556, 34, 10]
Insertion_sort(mydata)
print(mydata)