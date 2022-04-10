class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = '{0:08b}'.format(n)

        count = 0
        for s in st:
            if s=='1':
                count+=1
        return count
