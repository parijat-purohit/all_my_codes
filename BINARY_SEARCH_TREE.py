class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, num):
        if self.val == 0:
            self.val = num
        if num < self.val:
            if self.left:
                return self.left.insert(num)
            self.left = TreeNode(num)
        elif num > self.val:
            if self.right:
                return self.right.insert(num)
            self.right = TreeNode(num)


nums = [5,4,3,2,1]
bst = TreeNode()
for num in nums:
    bst.insert(num)
