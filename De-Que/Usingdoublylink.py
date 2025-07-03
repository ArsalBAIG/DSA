from DoublyLinkList import *

class Deque:

    def __init__(self):
        self.myDeque = DLL()
        self.item_count = 0

    def is_empty(self):
        return self.myDeque.is_empty()

    def insert_front(self, data):
        self.myDeque.insert_start(data)
        self.item_count += 1

    def insert_rare(self, data):
        if self.is_empty():
            raise IndexError('Deque Underflow')
        else:
            self.myDeque.insert_last(data)
            self.item_count -= 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError('Deque underflow!')
        else:
            self.myDeque.delete_first()
    
    def delete_rare(self):
        if self.is_empty():
            raise IndexError('Deque Underflow!')
        else:
            self.myDeque.delete_last()

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque underflow!')
        return self.myDeque.start.item
    
    def get_rare(self):
        if self.is_empty():
            raise IndexError('Deque underflow!')
        else:
            temp = self.myDeque.start
            while temp.next != None:
                temp = temp.next
            return temp.item
        
    def size(self):
        return len(self.item_count)
    
d = Deque()
d.insert_front(77)
d.insert_rare(88)
print(f"Front element is: {d.get_front()}")
print(f"Rare element is: {d.get_rare()}")