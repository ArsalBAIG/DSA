def linearSearch(array, item):
    for current in range(array):
        if array[current] == item:
            return current
    return None

array = [3, 5, 6, 8, 1]
item = 8
result = linearSearch(array, item)
print(f"Item is found at index: {result}")