class Node:
    def __init__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
            if self.righttchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True

    def find(self, data):
        if (self.value == data) :
            return True
        elif self.value > data :
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            return False

    def preorder(self):
        if self.leftchild:
            self.leftchild.preorder()
        elif self.rightchild:
            self.rightchild.preorder()

    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        elif self.rightchild:
            self.rightchild.postorder()

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        elif self.rightchild:
            self.rightchild.inorder()



class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root: #root exist
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        self.root.preorder()

    def postorder(self):
        self.root.postorder()

    def inorder(self):
        self.root.inorder()


bst = Tree()
print(bst.insert(10))
print(bst.insert(9))
print(bst.find(10))
print(bst.insert(9))
print(bst.find(3))

