class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = int((low+high)/2)
            print(low, high, mid)
            print(nums[mid], target)
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low = mid + 1
            elif target<nums[mid]:
                high = mid - 1
        return -1

s = Solution()
print(s.search([1,3,5,7,8,11], 7))