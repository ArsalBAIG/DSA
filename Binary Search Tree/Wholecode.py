# This code is for diff functions in BST.
class Node:
    def __init__(self, item= None, left= None, right= None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        # Recursive style: The BST subtrees are tree itself so we can use the same function for them. As a result, recursion is favorable.
        self.root = self.Rinsert(self.root, data) # Here, rinsert() func is a recursive func.
        #This recursive func will put the data of root tree that we provide it and return the ref of root tree.

    def Rinsert(self, root, data): # Here, root is the root of tree, & data is the data to be entered.
        if root is None:
            return Node(data)
        if data < root.item: #here, root means the left root of subtree
            root.left = self.Rinsert(root.left, data)
        elif data > root.item: #here, root means the right root of subtree
            root.right = self.Rinsert(root.right, data)
        return root #here, root means the top-most root of Tree.
    
    def search(self, data):
        return self.Rsearch(self.root, data)
    
    def Rsearch(self, root, data):
        if root is None:
            return Node(data)
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.Rsearch(root.left, data)
        else:
            return self.Rsearch(root.right, data)
    
    def Inorder(self):
        result = []
        self.Rinorder(self.root, result)
        return result
    
    def Rinorder(self, root, result):
        if root: # This conditon is True unless root is not None.
            self.Rinorder(root.left, result) # This is basically root node.
            result.append(root.item) # In order to access root node item we append it to the result which is our empty list.
            self.Rinorder(root.right, result)

    
    def Preorder(self):
        result = []
        self.Rpre_order(self.root, result)
        return result
    
    def Rpre_order(self, root, result):
        if root: # This conditon is True unless root is not None.
            result.append(root.item)
            self.Rpre_order(root.left, result)
            self.Rpre_order(root.right, result)
    
    def Rpost_order(self):
        result = []
        self.Rpost_order(self.root, result)
        return result
    
    def Rpost_order(self, root, result):
        if root: # This conditon is True unless root is not None.
            self.Rpost_order(root.left, result)
            self.Rpost_order(root.right, result)
            result.append(root.item)
    
    def min_value(self, temp): # temp points the root node of subtree.
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
        
    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item # This gives the item stored in current after the completion of loop.
    
    def delete(self, data):
        self.root = self.Rdelete(self.root, data)

    def Rdelete(self, root, data):
        if root is None:
            return root # root canbe replace with None.
        if data < root.item:
            root.left = self.Rdelete(root.left, data)
        elif data > root.item:
            root.right = self.Rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right # It means that if left side of root node is empty then see the right side  and after this the value is returend to the function root.left.
            elif root.right is None:
                return root.left
            # In case of, 2 childs.
            root.item == self.min_value(root.right) # min_value is used as a successor.
            self.Rdelete(root.right, root.item)
        return root
    
    def size(self):
        return len(self.Inorder())
    
