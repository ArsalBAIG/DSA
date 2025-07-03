# Step 1.

class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_start(self, data):
        n = Node(None, data, self.start)#coz we're inserting at start that's why we use self.start in place of next.
        if not self.is_empty():
            self.start.prev = n # we assign ref of new node 'n' to the start of prev node.
        self.start = n
    def insert_last(self, data):
        temp = self.start
        if self.start is None:
            temp = None
        else:
            if self.start is not None:
                while temp.next is not None:# it checks the next var of temp is not none bcz if none that means it is the last node and in this case the temp is in the second last node.
                    temp = temp.next # Here, when loops ends it contains the referrence of last node.
            n = Node(temp, data, None) #here, temp contains the ref of last node so when we creted a new node thus, we need temp as a prev member to represent the referrence.
            if temp == None: # checks if temp is none as mentioned in above code line if it is none which indicates that there only one node and it is assigned to the start node.
                self.start = n #assign ref of new node 'n' to self.start.
            else:
                temp.next = n
    
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            else:
                temp = temp.next 
            return None
        
    def insert_after(self,temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None: # checks that is it the last node or not.
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def delete_first(self):
        if self.start is not None: #checks is the list contains one node only
            self.start = self.start.next
            if self.start is not None: # means second node exsist
                self.start.prev = None
    
    def delete_last(self):
        temp = self.start
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            while temp is not None: 
                temp = temp.next # contains the ref of last node.
                temp.prev.next = None # here, this line referes to 2nd last node and when we put none in the next of this node it makes it the last node which alternatively eleminates the originally last node.

    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next # deletes the first node.
                    break
                temp = temp.next 
    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current: # means that if self.current is none.
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    
mylist = DLL()
mylist.insert_start('15')
mylist.insert_last('25')
mylist.insert_after(mylist.search(25), 20)
for x in mylist:
    print(x, end=' ')
print()