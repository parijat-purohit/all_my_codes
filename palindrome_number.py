"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
Be careful about the negative numbers.
I didn't use reverse string in the solution.

https://leetcode.com/problems/palindrome-number/
"""
class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num<0:
            return False
        tempNum=num
        count = 0
        revNum = 0
        numlist = []
        while(tempNum>0):
            numlist.append(tempNum%10)
            tempNum=int(tempNum/10)
            count+=1

        for i, n in enumerate(numlist):
            revNum+=numlist[i]*pow(10,count-i-1)

        if num==revNum:
            return True
        else:
            return False
