class Node:

    def __init__(self, item, priority, next):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    
    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def is_empty(self):
        return self.start == None
    
    def push(self, data, priority):
        n = Node(data, priority, None)
        if not self.start or priority < self.start.priority: #here, it means priority of new elemnet n is lesser than priority of current element.
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next != None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next # The new node is inserted before the first node.
            temp.next = n
        self.item_count += 1
    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue Underflow!')
        data = self.start.item # the data of first node is stored in data variable.
        self.start = self.start.next
        self.item_count -= 1
        return data
    def size(self):
        return self.item_count
    
p = PriorityQueue()
p.push('Ahemd', 8)
p.push('Akram', 2)
p.push('Ai', 7)

while not p.is_empty():
    print(p.pop())