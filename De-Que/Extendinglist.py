class Deque(list):

    def is_empty(self):
        return len(self) == 0
    
    def insert_front(self, data):
        self.insert(0, data)

    def insert_rear(self, data):
        if self.is_empty():
            raise IndexError('Deque Underflow!')
        else:
            self.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError('Deque Underflow!')
        else:
            self.pop(0)
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Deque Underflow!')
        else:
            self.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque Underflow!')
        else:
            return self[0]
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque Underflow!')
        else:
            return self[-1]
        
    def size(self):
        return len(self)
    
dq = Deque()
dq.insert_front(22)
dq.insert_front(33)
dq.insert_rear(44)
dq.insert_rear(55)
print(f"Front element is: {dq.get_front()}")
print(f"Rare element is: {dq.get_rear()}")