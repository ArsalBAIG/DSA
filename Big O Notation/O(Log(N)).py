def binary_search(arr, target):
# Here, left is assign 0 and right is assign the end of the array.
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
# Here, if mid array is less than target then it means target is at the right side.
        elif arr[mid] < target:
            left = mid + 1
# Here, if not true the above condition then it means target is at the left side.
        else:
            right = mid - 1
    return -1
    
arr = [1,2,3,4,5,6,7,8]
target = 7
result = binary_search(arr, target)
print(result)