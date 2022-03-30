"""
An innovative way to find out the square root of a number without using prebuilt functions like sqrt(x) or pow(num,0.5)
"""
def squareroot(x):
    low = 0
    high = x
    while(high-low>0.0000000000000001): # change your precision here or add steps for how long you want to bisect!
        mid = (low+high)/2
        if mid*mid> x:
            high=mid
        elif mid*mid==x:
            return mid
        else:
            low = mid
    return mid
print(squareroot(68))
print(squareroot((64)))
