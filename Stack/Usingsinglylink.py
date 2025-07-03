from SinglyLinkList import *

class Stack:
    def __init__(self):
        self.mysll = SLL()
        self.itemCount = 0 # to increment value.
    def is_empty(self):
        return self.mysll.is_empty()
    
    def push(self, data): # Remember, in Stack we push() and pop() data at the same end whether at starting or at ending.
        self.mysll.insert_at_start(data)
        self.itemCount += 1

    def pop(self):
        if not self.is_empty():
            self.mysll.delete_first()
            self.itemCount += 1

    def peek(self):
        if not self.is_empty():
            return self.mysll.start.item # mysll is pointing first element of node and we're printing the first element.
        
    def size(self):
        return self.itemCount

s = Stack()
s.push(44)
s.push(32)
s.push(90)
print(f"Popped No is: {s.pop()}") # bcz we have used SinglyLinkList Object as a Stack Object that's why it is showing None as a Popped No.
print(s.peek())
print(f"Size is: {s.size()}")