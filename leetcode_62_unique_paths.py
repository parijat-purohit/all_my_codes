class Solution(object):
    res = {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1
        if m==0 or n==0:
            return 0
        if (m,n) in self.res.keys(): #this memoization helped me to avoid TLE
            return self.res[m,n]
        a = self.uniquePaths(m-1, n)
        b = self.uniquePaths(m,n-1)

        self.res[m,n] = a+b
        return a+b
