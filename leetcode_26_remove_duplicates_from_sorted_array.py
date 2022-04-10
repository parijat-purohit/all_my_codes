class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurence = {}
        for i, n in enumerate(nums):
            if i<len(nums)-1:
                if nums[i] == nums[i+1]:
                    if n not in occurence.keys():
                        occurence[n] = 1
                    else:
                        occurence[n] += 1

        for o in occurence:
            print(o, occurence[o])
            if occurence[o]!=0:
                for i in range(occurence[o]):
                    nums.remove(o)
                    occurence[o]-=1
