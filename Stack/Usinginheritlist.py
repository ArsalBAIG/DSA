class Stack(list): # list is parent calss of Stack.

    def is_empty(self):
        return len(self) == None
    
    def push(self, data):
        self.append(data) # We use append method bcz it is the method of list class which is a parent class in this case.

    def pop(self):
        if not self.is_empty():
    # Note: Stack also contain pop method while List which is a parent class also contain pop() method. As a result, when we call pop() method of list class due to Overriding pop method of Stack is called. To avoid this follow below:
            return super().pop() #Here, we explicitly use the pop() method of parent.
        else:
            raise IndexError("Stack is Empty!")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty!")
        
    def size(self):
        return len(self)

    def insert(self, index, data): # In this fun, we're overriding the insert() method bcz we have insert() method in both of parent and child class.
        raise AttributeError("No attribute of 'insert' method in Stack.")
    
s1 = Stack()
s1.push(54)
s1.push(99)
s1.push(33)
print(s1.peek())
print(f'Size is: {s1.size()}')