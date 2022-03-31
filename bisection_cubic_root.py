"""
An innovative way to find out the cubic root of a number. We use bisection method.
"""
def cuberoot(x):
    low = 0
    high = x
    while(high-low>0.000001): # change your precision here or add steps for how long you want to bisect!
        mid = (low+high)/2
        if mid*mid*mid> x:
            high=mid
        elif mid*mid*mid==x:
            return mid
        else:
            low = mid
    return round(mid, 3)
print(cuberoot(68))
print(cuberoot(64))
print(cuberoot(125))
