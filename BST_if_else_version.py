class Node():
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

    def insert(self, num):
        if self.val == 0:
            self.val = num
        elif num < self.val:
            if self.left:
                self.left.insert(num)
            else:
                self.left = Node(num)
        else:
            if self.right:
                self.right.insert(num)
            else:
                self.right = Node(num)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

n = Node()
x = [5,3,8,2,11,4]
for num in x:
    n.insert(num)
n.inorder()
