"""
https://leetcode.com/problems/roman-to-integer/
Convert Roman Characters to Integer
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        prev = ''
        for d in s:
            print(d)
            if d == 'I':
                count+=1
            elif d == 'V':
                if prev == 'I':
                    count += 3
                else:
                    count+=5
            elif d == 'X':
                if prev == 'I':
                    count+=8
                else:
                    count+=10
            elif d == 'L':
                if prev == 'X':
                    count+=30
                else:
                    count+=50
            elif d == 'C':
                if prev == 'X':
                    count+=80
                else:
                    count+=100
            elif d == 'D':
                if prev == 'C':
                    count+=300
                else:
                    count+=500
            elif d == 'M':
                if prev == 'C':
                    count+=800
                else:
                    count+= 1000
            prev = d
        return count
