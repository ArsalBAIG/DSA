from SinglyLinkList import *

class Stack(SLL):

    def __init__(self):
        super().__init__() # In python, the constructor of child class doesn't call constructor of parent class that why we have to use super() method. 
        self.item_count = 0

    def is_empty(self):
        return super().is_empty() # Explicitly calling.
    
    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -= 1
        else:
            raise IndexError('Stack was Empty!')
            
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Stack was Empty!')
    
    def size(self):
        return self.item_count
    
s = Stack()
s.push(33)
s.push(89)
s.push(44)
print(f"Popped no is: {s.pop()}")
print(s.peek())
print(f"Size is: {s.size()}")