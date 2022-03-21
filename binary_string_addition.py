"""
Given two binary strings a and b, return their sum as a binary string.

https://leetcode.com/problems/add-binary/
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxlen = len(a) if len(a)>len(b) else len(b)
        len_a = len(a)
        len_b = len(b)
        for i in range(maxlen):
            if i>=len_a:
                a = '0'+a
            if i>=len_b:
                b = '0'+b
        summation = ''
        carry = 0
        for i in reversed(range(maxlen)):
            if int(a[i]) + int(b[i]) + carry == 3:
                summation += '1'
                carry = 1
            elif int(a[i]) + int(b[i]) + carry == 2:
                summation += '0'
                carry = 1
            elif int(a[i]) + int(b[i]) + carry == 1:
                summation += '1'
                carry = 0
            else:
                summation += '0'
                carry = 0
        if carry == 1:
            summation += '1'
        return summation[::-1]
