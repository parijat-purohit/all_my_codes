class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, num):
        if self.val == 0:
            self.val = num
            return self.val
        if not self.left:
            self.left = TreeNode(num)
        elif not self.right:
            self.right = TreeNode(num)
        else:
            return self.left.insert(num)
            return self.right.insert(num)
    def inorder(self):
        inlist = []
        if self.left:
            self.left.inorder()
        inlist.append(self.val)
        if self.right:
            self.right.inorder()
        return inlist

nums = [1,2,3]
bt = TreeNode()
for num in nums:
    bt.insert(num)
print(bt.inorder())
