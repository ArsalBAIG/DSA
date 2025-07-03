class Node:
    def __init__(self, item= None, next= None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self): # self canbe replaced with top. 
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item # We're placing the first item of node in the 'data' var bcz in pop we want to show the deleted value so in order to use return 'data' method we have to store it in 'data' var.
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError('Stack was Empty!')
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack was Empty!")
        
    def size(self):
        return self.item_count

s = Stack()
s.push(44)
s.push(77)
s.push(99)
print(f"Poped Element is: {s.pop()}")
print(f"Top Element is: {s.peek()}")