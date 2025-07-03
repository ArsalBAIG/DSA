class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0 # it will return True when lenght is 0 means there's no item in list.
    
    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError('Stack was Empty!')
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1] # -1 is the index of last element in the list.
        else:
            raise IndexError('Stack was Empty!')
        
    def size(self):
        return len(self.items)
    
s1 = Stack()
s1.push(44)
s1.push(55)
s1.pop()
print(s1.peek())
print()