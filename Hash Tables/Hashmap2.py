class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]  # This is a list comprehension.

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # ord is used to get ASCII code.
        return h % self.max  # 100 is the size of array.

    def __setitem__(self, key, value):
        h = self.get_hash(key)  # Calculate hash-value for a key.
        found = False
        for idx, element in enumerate(self.arr[h]):  # Iterate through the corresponding list.
            if element[0] == key:
                self.arr[h][idx] = (key, value)  # Update the value if key is found.
                found = True
                break
        if not found:
            self.arr[h].append((key, value))  # Append the new key-value pair if key is not found.

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:  # Iterate through the corresponding array.
            if element[0] == key:  # Check if the key matches.
                return element[1]  # Return the value if key is found.
        return None  # Return None if key is not found.

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]  # Delete the key-value pair if key is found.
                return

# Example usage
t = HashTable()
t["march 8"] = 90
t["march 8"] = 99
print(t["march 8"])  # Corrected print statement
print(t.arr)