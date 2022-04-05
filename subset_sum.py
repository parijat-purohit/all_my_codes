"""
You are given an array and you are asked can you make amount s out of it? easy huh?
given arr = [1,2,3,4,5] if I ask, can you make 7, the naive approach would be iterate
through the array n^2 times and see whether the sum of two elements equal to 7 or not.

But if I ask you how many ways you can make 7 out of it. huge difference!! huge!!!
We need DP here... sigh
"""
def subsetsum(i, s):
    if s == w: # reached the target
        return 1
    if i==n: # already iterated the entire array
        return 0
    if res[i][s] != -1: # calculated the value before. 
        return res[i][s]
    a = subsetsum(i+1, s+arr[i]) # taking the value
    b = subsetsum(i+1, s) # not taking the value
    res[i][s] = a + b
    return res[i][s] # always 0 0. That's where our result stays!


arr = [3,4,1,2,5,6]
n = len(arr)
res = [[-1]*100]*100
w = 7
print(subsetsum(0, 0))
