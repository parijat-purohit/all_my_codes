class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        for v in d:
            if d[v] == 1:
                return v
