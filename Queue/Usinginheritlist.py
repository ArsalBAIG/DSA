class Queue(list):

    def is_empty(self):
        return len(self) == None
    
    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError('Queue Underflow!')
    
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('Queue Underflow!')
        
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Queue Underflow!')
        
    def size(self):
        return len(self)
q = Queue()
q.enqueue(77)
q.enqueue(88)
q.enqueue(99)
q.dequeue()
print(f"Front is: {q.get_front()}")
print(f"Rear is: {q.get_rear()}")