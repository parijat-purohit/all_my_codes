class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        finalst = ""
        minlen = 201
        cnt = 0
        if len(strs) == 1:
            return strs[0]
        for st in strs:
            if len(st)==0:
                return ""
            if st[0]!= strs[0][0]:
                return ""
            if len(st) < minlen:
                minlen= len(st)


        for i in range(minlen):
            for j in range(len(strs)-1):
                if(strs[j][i]==strs[j+1][i]):
                    x = strs[j][i]
                else:
                    x = ""
                    break
            if x == "":
                break
            finalst+=x
        return finalst
