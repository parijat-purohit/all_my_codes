# I love this problem. It's actually fibonacci series you are having here :)
class Solution(object):
    res=[-1]*46
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1;
        if self.res[n]!=-1:
            return self.res[n]
        a = self.climbStairs(n-1)
        b = self.climbStairs(n-2)
        self.res[n] = a+b
        return self.res[n]
