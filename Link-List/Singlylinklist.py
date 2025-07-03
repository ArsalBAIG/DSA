class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
    
class SLL:
    # Driver code.
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data, self.start) # self.start is a reference to the next node.
        self.start = n # here, n rep starting node & we give a reference of new node to the starting node.
    
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty(): # Checks wheather node is empty or not
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next # move further/ onward.
            temp.next = n # here, assign the reference of next to the new node n.

    def search(self, data):
        temp = self.start # starting from the list.
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next #here, it moves to the next node.
        return None
    
    def insert_after(self, temp, data): #here, we insert data after temp.
        if temp is not None:
            n = Node(data, temp.next) #temp.next rep the reference of the next node after this current node.
            temp.next = n #here, we assign reference of current node to the previous node.

    def printList(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end = " ")
            temp = temp.next 

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next # Here, our first node is removed.

    def delete_last(self):
        if self.start is not None:
            pass
        elif self.start is None: #means list has only one node.
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None: # here, temp.next.next means third node & int the second iteration temp.next.next means last node.
                temp = temp.next # After second iteration temp is to second-last node. 
            temp.next = None # Here, fourth or last node is set to none or del.

    def delete_item(self, data):
        if self.start is None:
            pass
        if self.start.item == data: #Here, it checks if the desired item is present in the first node if it is then
                self.start = self.start.next # it is deleted by using self.start.next.  
                return
        else:
                temp = self.start
                if temp.item == data:
                    self.start = temp.next # means reference of second node comes in the frist/ start node. which means the node is deleted.
                else:
                    while temp.next is not None:
                        if temp.next.item == data: # here, temp jis next ko point kr rha ha agar wo item data k equal ha too..
                            temp.next = temp.next.next # points next to next element bcz we point a value before the value we want to del that's why we use next to next in our code.
                            break
                        temp = temp.next
# When i have to make my class(SLL()) iterateable then i have to make another class.

    def __iter__(self):
        return SLLiterator(self.start) #link-list wala start ha.
    
class SLLiterator:
    def __init__(self, start):# Here, current is like a temp in the above class.
        self.current = start # this start is not a link-list start.
    # first make iterater to make it iterable.
    # making iterater.
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current: #means if value of current is none the loops stops to iterate.
            raise StopIteration # to stop repetation
        data = self.current.item #put the item in current in data.
        self.current = self.current.next # giving ref to the next data.
        return data


myList  = SLL()
myList.insert_at_start('55')
myList.insert_at_last('77')
search_node = myList.search('55')
myList.insert_after(search_node, '66')
myList.delete_item('55')
myList.printList()

myList.printList()
for x in myList:
    print(x, end= " ")

print()