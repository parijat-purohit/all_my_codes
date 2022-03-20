"""
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.
"""
def missing(arr):
    arr = sorted(arr)
    for ind, val in enumerate(arr):
        if ind+1 != val:
            return ind + 1
a = [4,2,1,5]
print(missing(a))
