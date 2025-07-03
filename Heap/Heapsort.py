class Heap:
    def __init__(self):
        self.myheap = []

    def create_heap(self, list1):
        for i in list1:
            self.insert(i)

    def insert(self, i):
        index = len(self.myheap) # New element is inserted at the end of list initially and stored in index.
        parent_index = (index - 1) // 2
        while index > 0 and self.myheap[parent_index] < i: # The loops continues until the parent is smaller than current element.
            if index == len(self.myheap):
                self.myheap.append(self.myheap[parent_index]) # Here, append cretes a copy of element bcz in list in order to imagine a node we that is not created yet. So, we use the append func.
            else:
                self.myheap[index] = self.myheap[parent_index] # If the element isn't at the end of list then replaces element at index with parent's value.
            index = parent_index
            parent_index = (index - 1) // 2
        if index == len(self.myheap): # to check the index is at the last of the list. if it is then append it.
            self.myheap.append(i)
        else:
            self.myheap[index] = i
    
    def top(self):
        if len(self.myheap) == 0:
            raise EmptyHeapException()
        return self.myheap[0]
    def delete(self):
        if len(self.myheap) == 0:
            raise EmptyHeapException()
        if len(self.myheap) == 1:
            return self.myheap.pop()
        max_value = self.myheap[0] # Here, we just copy the element. The max_vlaue stores the root node.
        temp = self.myheap.pop() # Here, temp points the last element. # pop() generally deletes the last element.
        index = 0 # As in above code the index is pointing the last element here, index is pointing the first element.
        leftChild_index = 2 * index + 1
        rightChild_index = 2 * index + 2
        while leftChild_index < len(self.myheap): # At least one child exsists.
            if rightChild_index < len(self.myheap):
                if self.myheap[leftChild_index] > self.myheap[rightChild_index]:
                    if self.myheap[leftChild_index] > temp:
                        self.myheap[index] = self.myheap[leftChild_index]
                        index = leftChild_index
                    else:
                        break
                else:
                    if self.myheap[rightChild_index] > temp:
                        self.myheap[index] = self.myheap[rightChild_index]
                        index = rightChild_index
                    else:
                        break
            else: # For no Right-child.
                if self.myheap[leftChild_index] > temp:
                    self.myheap[index] = self.myheap[leftChild_index]
                    index = leftChild_index
                else:
                    break
            leftChild_index = 2 * index + 1
            rightChild_index = 2 * index + 2
        self.myheap[index] = temp
        return max_value
    
    def heapSort(self, list1):
        self.create_heap(list1)
        list2 = []
        try:
            while True:
                list2.insert(0, self.delete()) # Remove the max_element from the list then insert it in list2 at the start.
        except EmptyHeapException:
            pass
        return list2
    
class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap!"):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
list1 = [23, 56, 92, 12, 39, 45, 67]
h = Heap()
list1 = h.heapSort(list1)
print(list1)