class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        low = 0
        high = x
        for i in range(32):
            mid = (low + high) / 2
            if mid * mid > x:
                high = mid
            elif mid * mid == x:
                return mid
            else:
                low = mid
        return int(round(mid,2))
