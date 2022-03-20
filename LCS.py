"""
Longest Common Subsequence Problem solution in Python
"""
a = [[-1 for i in range(100)] for i in range(100)]
st1 = 'ABCDABC'
st2 = 'CDAB'

def LCS(X,Y,m,n):
    if m==len(st1) or n==len(st2):
        return 0
    elif a[m][n]== -1:
        if(X[m]==Y[n]):
            a[m][n] = 1+LCS(X, Y, m+1, n+1)
        else:
            a[m][n] = max(LCS(X, Y, m+1, n),
                              LCS(X, Y, m, n+1))
    return a[m][n]

print(LCS(st1, st2, 0, 0))
