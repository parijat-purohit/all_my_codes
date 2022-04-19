class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        t = ""
        for x in s.lower():
            if (x>='a' and x<='z') or (x>='0' and x<='9'):
                t+=x
        if len(t) == 0:
            return True
        import math
        if len(t)%2==0:
            halfway = math.ceil((len(t)/2))
        else:
            halfway = math.ceil((len(t)/2)) - 1

        for i in range(int(halfway)):
            if t[i]!=t[len(t) -1 - i ]:
                return False
        return True
