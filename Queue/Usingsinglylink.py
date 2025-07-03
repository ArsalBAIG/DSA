from SinglyLinkList import *

class Queue:
    def __init__(self):
        self.myQueue = SLL()
        self.item_count = 0
            

    def is_empty(self):
        return self.myQueue.is_empty()
    
    def enqueue(self, data):
        self.myQueue.insert_at_start(data)
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            self.myQueue.delete_first()
            self.item_count -= 1
        else:
            raise IndexError('Queue Underflow!')
        
    def get_front(self):
        if not self.is_empty():
            return self.myQueue.start.item
        else:
            raise IndexError('Queue Underflow!')
    
    def get_rear(self):
        if not self.is_empty():
            temp = self.myQueue.start
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError('Queue Underflow!')
            
    def size(self):
        return self.item_count

q = Queue()
q.enqueue(44)
q.enqueue(55)
q.enqueue(66)
print(f"Front value is: {q.get_front()}") # FIFO(First In First Out)
print(f"Rear value is: {q.get_rear()}")