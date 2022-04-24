class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i, char in enumerate(s):
            # normal swap
            if i<len(s)/2:
                diff = len(s) - i -1
                s[i], s[diff] = s[diff], s[i]
