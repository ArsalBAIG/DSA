class PriorityQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data,priority):
        index = 0       #[index][0] indicates data & [index][1] means priority number.
# Here, in while loop it ensure the loop doesn't go beyound the list and in the second phase it compares the priority of current item(store at index) with new item's priority.
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data,priority)) #if item(which is a tuple) is found then it is insert to the list at index.
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue is Empty!')
        return self.items.pop(0)[0] #[0] indicates data in the tuple.
    
    def size(self):
        return len(self.items)
    
pq = PriorityQueue()
pq.push(33, 7)
pq.push(44, 9)
pq.push(55, 2)

while not pq.is_empty():
    print(pq.pop())