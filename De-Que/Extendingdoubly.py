from DoublyLinkList import *

class Deque:
    def __init__(self):
        self.front = None
        self.rare = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None
    
    def insert_front(self, data):
        n = Node(None, data, self.front)
        if self.is_empty():
            self.rare = n
        else:
            n.next = self.front
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rare(self, data):
        n = Node(self.rare, data, None)
        if self.is_empty():
            self.front = n
        else:
            self.rare.next = n
            n.prev = self.rare
        self.rare = n
        self.item_count += 1
    
    def remove_front(self):
        if self.is_empty():
            raise IndexError('Deque is Empty!')
        elif self.front == self.rare:
            self.front = self.rare = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1
    
    def remove_rare(self):
        if self.is_empty():
            raise IndexError('Deque is Empty!')
        elif self.front == self.rare:
            self.front = self.rare = None
        else:
            self.rare = self.rare.next
            self.rare.next = None
        self.item_count -= 1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is Empty!')
        return self.front.item
    
    def get_rare(self):
        if self.is_empty():
            raise IndexError('Deque is Empty!')
        return self.rare.item
    
    def size(self):
        return self.item_count
    
d = Deque()
d.insert_front(33)
d.insert_front(44)
d.insert_rare(88)
d.insert_rare(99)
print(f"Front element is: {d.get_front()}")
print(f"Rare element is: {d.get_rare()}")