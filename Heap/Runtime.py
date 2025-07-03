def BinarySearch(array, item, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid]:
            return mid
        elif item > array[mid]:
            return BinarySearch(array, item, mid + 1, high)
        else:
            return BinarySearch(array, item, mid - 1, high)
    return None

array = [ 23, 92, 0, 90, 12, 45, 76]
item = 45
array.sort()
result = BinarySearch(array, item, 0, len(array) - 1)