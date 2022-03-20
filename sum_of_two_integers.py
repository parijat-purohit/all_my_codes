"""
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.
PYTHON

O(n^2) soln. Not good.
A better O(n) soln is in the internet. I just keep track of it because I implemented it.
"""
def sumton(arr,n):
    arr = sorted(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i]+arr[j]) == n and i!=j:
                return True
    return False
a = [4,2,3,5]
print(sumton(a,5))
print(sumton(a,10))
