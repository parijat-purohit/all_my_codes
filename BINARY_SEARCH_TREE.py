class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, num):
        if self.val == 0:
            self.val = num
            return self.val
        if num < self.val:
            if self.left:
                return self.left.insert(num)
            self.left = TreeNode(num)
        elif num > self.val:
            if self.right:
                return self.right.insert(num)
            self.right = TreeNode(num)

    def preorder(self):
        print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
           self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val)


nums = [50,4,60,2,20,70,40,25]
bst = TreeNode()
for num in nums:
    bst.insert(num)
print("Printing Preorder Output")
bst.preorder()
print("\nPrinting Inorder Output")
bst.inorder() #we should expect a sorted output
print("\nPrinting Postorder Output")
bst.postorder()
