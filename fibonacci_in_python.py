"""
Intro to Dynamic Programming.
How about Fibonacci series.
1,1,2,3,5,8,13,21,...
"""
# SOLUTION 1

# initializing an array a with -1, meaning it has nothing in it.

a=[-1]*10000
# It's cool to initialize the array. Isn't it?

def fibo(n): # n means what term of the fibonacci series
    if(n==1 or n==2): # This is the base case. Every DP soln must have base cases like this.
        return 1
    if(a[n]==-1):
        a[n] = fibo(n-1) + fibo(n-2)
    
    return a[n]

# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))
# print(fibo(5))
# print(fibo(6))
# Question: you could do it without the array what's the purpose of using this a[n] array?

# SOLUTION 2

def FIBO(n):
    if(n==1 or n==2):
        return 1
    return FIBO(n-1) + FIBO(n-2)

# Only 3 lines of code!!! But remember the first solution is still better. Because it's O(n).

# print(FIBO(1))
# print(FIBO(2))
# print(FIBO(3))
# print(FIBO(4))
# print(FIBO(5))
# print(FIBO(6))
