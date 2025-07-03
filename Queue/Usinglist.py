class Queue:

    def __init__(self):
        self.items = []
        # self.front = None
        # self.rear = None

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, data): # for inserion
        self.items.append(data)
        
    def dequeue(self): # for deletions
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('Queue is Empty!')

    def get_front(self):
        if not self.is_empty():
            return self.items[0] # gets the oldest element.
        else:
            raise IndexError('Queue is Empty!')
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Queue is Empty!')
        
    def size(self):
        return len(self.items)
    
q = Queue()
q.enqueue(34)
q.enqueue(99)
q.enqueue(77)
q.dequeue()
print(q.get_front())
print(q.get_rear())
# Note: As 34 is the oldest entered item so when we call dequeue() it will delete the oldest item which is 34. After this when i print get_front() then it will print 99 and then 77 in a sequence of queue.