class Node:

    def __init__(self, item= None, left= None, right= None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.Rinsert(self.root, data)

    def Rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.Rinsert(root.left, data)
        elif data > root.item:
            root.right = self.Rinsert(root.right, data)
        return root
    
    def search(self, data):
        return self.Rsearch(self.root, data)
    
    def Rsearch(self, root, data):
        if root is None:
            return Node(data)
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.root(root.left, data)
        else:
            return self.root(root.right, data)
        
    def Inorder(self):
        result = []
        self.Rinorder(self.root, result)
        return result
    
    def Rinorder(self, root, result):
        if root:
            self.Rinorder(root.left, result)
            result.append(root.item)
            self.Rinorder(root.right, result)

    def Preorder(self):
        result = []
        self.Rpreorder(self.root, result)
        return result
    
    def Rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.Rpreorder(root.left, result)
            self.Rpreorder(root.right, result)

    def Postorder(self):
        result = []
        self.Rpostorder(self.root, result)
        return result
    
    def Rpostorder(self, root, result):
        if root:
            self.Rpostorder(root.right, result)
            self.Rpostorder(root.left, result)
            result.append(root.item)
    
    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item
    
    def delete(self, data):
        self.root = self.Rdelete(self.root, data)

    def Rdelete(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.Rdelete(root.left, data)
        elif data > root.item:
            root.right = self.Rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item == self.max_value(self.left)
            self.Rdelete(root.left, data)
        return root
    
    def size(self):
        return len(self.Inorder())