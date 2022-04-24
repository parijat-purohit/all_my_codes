class Solution:
    def countBits(self, n: int):
        l = []
        for i in range(n+1):
            count = 0
            while(i):
                if i%2==1:
                    count+=1
                i = i>>1
            l.append(count)
        return l
