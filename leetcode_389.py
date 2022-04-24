"""
https://leetcode.com/problems/find-the-difference/
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dup = []
        s_count = 0
        t_count = 0
        for i in range(len(s)):
            s_count += ord(s[i])
            t_count += ord(t[i])
        t_count += ord(t[-1])
        return chr(t_count - s_count)
