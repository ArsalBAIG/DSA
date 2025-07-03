class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_begin(self, data):
        n = Node(None, data, None)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev  # last node.
            self.start.prev.next = n
            self.start.prev = n
            self.start = n  # start pointing to new node.

    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start
        if temp is None:
            return None
        while temp != self.start:  # Traversing
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.start:
                break
        return None
        
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(None, data, None)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n

    def printList(self):
        if self.is_empty():
            return
        temp = self.start
        print(temp.item, end=' ')
        temp = temp.next
        while temp != self.start:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def delete_first(self):
        if self.is_empty():
            return
        if self.start.next == self.start:  # Single node case
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next
    
    def delete_last(self):
        if self.is_empty():
            return
        if self.start.next == self.start:  # Single node case
            self.start = None
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:  # Special Case
                self.delete_first()
            else:
                temp = temp.next
                while temp != self.start:
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                        break

    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:  # Ensure only one cycle
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        self.count = 1
        return data

# Testing the list
mylist = CDLL()
mylist.insert_at_begin('55')
mylist.insert_at_begin('77')
mylist.insert_at_last('99')
mylist.insert_after(mylist.search('99'), 33)
mylist.printList()
