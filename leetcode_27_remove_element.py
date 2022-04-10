class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        occurence = 0
        for n in nums:
            if n==val:
                occurence+=1
        for x in range(occurence):
            nums.remove(val)
