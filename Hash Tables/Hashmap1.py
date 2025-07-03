class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)] # This is a list comprehension.

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char) # ord is used to get ASCII code.
        return h % self.max # 100 is the size of array.

    # Creating a func to add a key-value pair
    def  add(self, key, value):
        h = self.get_hash(key) # getting the hash-value.
        self.arr[h] = value  # In order to add the value we have to store it in value.

    # Creating a func to get a key-value pair

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    # Creating a func to delete a key-value pair
    def delete(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

        
t = HashTable()
t.get_hash('march 7')
t.add('march 8', 222)
t.delete('march 8')
print(t.get('march 8'))