class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n # new node is added to the end of the queue by pointing next to the current rare node.
        self.rear = n
        self.item_count += 1

    def deequeue(self):
        if self.is_empty():
            raise IndexError('Empty Queue!')
        elif self.front == self.rear: # Here, it indicates queue wasn't empty bcz if it is empty then upper if condition will be run instead of elif.
            self.front = None # for single node(Special Case)
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError('Queue Empty!')
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Queue Empty!')
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.deequeue()
print(q.get_front())
print(q.get_rear())