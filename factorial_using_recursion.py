"""
Given a number n. Find out n! (factorial)
PYTHON
"""
def factorial(n):
    # we write the base case here
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

"""
Recursion tree looks like this:
5*factorial(4)              5*24=120
    |                        /\
    |                         |
   \/                         |
4*factorial(3)              4*6=24
    |                        /\
    |                         |
   \/                         |
3*factorial(2)              3*2=6
    |                        /\
    |                         |
   \/                         |
2*factorial(1)              2*1=2
    |                        /\
    |                         |
   \/                         |
  returning 1 ---------------->
"""
