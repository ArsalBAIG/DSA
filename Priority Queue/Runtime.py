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
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next != None and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
            self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('PriorityQueue Underflow!')
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data
    
    def size(self):
        return self.item_count
    
p = PriorityQueue()
p.push(33, 9)
p.push(44, 4)
p.push(22, 0)

while not p.is_empty():
    print(p.pop())