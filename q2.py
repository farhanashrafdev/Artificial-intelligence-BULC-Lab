class Node:
    def _init_(self,value=None):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def _init_(self):
        self.root = None

    def insertion(self,value):
        if  self.root == None:
            self.root = Node(value)
        else:
            self.insertNext(value,self.root)

    def insertNext(self,value,current_node):
        if value < current_node.data:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insertNext(value,current_node.left)

        elif value > current_node.data:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insertNext(value,current_node.right)
        elif value == current_node.data:
            if current_node.left is None:
                current_node.left = Node(value)
            if current_node.right is not None:
                current_node.left.left = Node(value)
            

    def search(self,value):
        if self.root:
            is_found = self.secondary_search(value,self.root)
            if is_found:
                return True
            return False
        else:
            return None
    def secondary_search(self,value,current_node):
        if value > current_node.data and current_node.right:
            print("The Value exists on the right side")
            return self.secondary_search(value,current_node.right)
        elif value < current_node.data and current_node.left:
            print("The value exists on the left side")
            return self.secondary_search(value,current_node.left)
        if value == current_node.data:
            print("The value is a node")
            return True

obj = BST()

obj.insertion(5)
obj.insertion(4)
obj.insertion(6)
obj.insertion(7)
obj.insertion(8)
obj.insertion(5)
obj.insertion(4)
obj.insertion(3)
obj.insertion(2)
obj.insertion(1)

print(obj.search(4))