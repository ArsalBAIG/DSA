class Node:
    def __init__(self, item= None, next= None): 
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last= None):
        self.last = last
    
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self, data):
        n = Node(data, None)
        if self.is_empty(): # Checks is the list empty.
            n.next = n # current node 'n' becomes first node.
            self.last = n # current node 'n' becomes last node.
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self, data):
        n = Node(data) # next has by-default None.
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n # Here, it indicates the new node is the new last node.

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next # next pointer points to first node.
        while temp != self.last: # The loop runs from first node to second-last node.
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data: # This is for the last node.
            return temp
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last: # This is done for the last node as if statement runs from start to 2nd last node except last node so this process is done.
                self.last = n 

    def printList(self):
        if self.is_empty():
            return
        temp = self.last.next
        while True: 
            print(temp.item, end=' ')
            temp = temp.next
            if temp == self.last.next:
                break
        print()


    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last: # means it points itself which in result means list has one node only.
                self.last = None
            else:
                self.last.next = self.last.next.next # means it shows the ref of second node which in result deletes the first node.

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last: # for single node.
                self.last = None
            else:
                temp = self.last.next
                while temp.next.next != self.last: # temp jese hee second last node per ho iske next ma first node k reference dal do which in result deletion of last node.
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp # here, temp is last node and it is deleted.

    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last:  # For single node
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:  # Delete first node
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp.next != self.last and temp.next.item != data:
                        temp = temp.next
                    if temp.next.item == data:
                        if temp.next == self.last:
                            self.delete_last()
                        else:
                            temp.next = temp.next.next
    
    
    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
                
class CLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start # used to store the ref of first node.
        self.is_first_iteration = True

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None: # means list is empty
            raise StopIteration
        if self.current == self.start and not self.is_first_iteration:
            raise StopIteration
        self.is_first_iteration = False
        data = self.current.item
        self.current = self.current.next
        return data

mylist = CLL()
mylist.insert_at_start('22')
mylist.insert_at_last('44')
mylist.insert_after(mylist.search('22'), 33)
for x in mylist:
    print(x, end=' ')
print()
mylist.printList()