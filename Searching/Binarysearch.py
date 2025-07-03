def BinarySearch(array, item, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if item == array[mid]:
            return mid
        elif item > array[mid]:
            return BinarySearch(array, item, mid + 1, high)
        else:
            return BinarySearch(array, item, low, mid - 1)
    else:
        return None
    
array = [34, 54, 9, 45, 21, 78]
item = 21
array.sort()
result = BinarySearch(array, item, 0, len(array) - 1)
print(result)