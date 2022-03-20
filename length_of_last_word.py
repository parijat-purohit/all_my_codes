"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

https://leetcode.com/problems/length-of-last-word/
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = s.split(" ")

        while '' in st:
            st.remove('')

        return len(st[len(st)-1])
