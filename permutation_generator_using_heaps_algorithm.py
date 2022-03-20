"""
PERMUTATION GENERATOR using HEAP's algo
Implementing Heap's algorithm as it is here.
https://en.wikipedia.org/wiki/Heap%27s_algorithm
Did some tricks to deal with strings.
if you are okay with list then you don't have to do the conversions in line 9 and 25
"""
def permutation_generator(i,A):
    if i==1:
        toprint = ''.join(map(str, st))
        print(toprint)
    else:
        permutation_generator(i-1,A)
    for j in range(i-1):
        if i%2==0:
            tmp = A[i-1]
            A[i-1] = A[j]  # Old fashioned swapping is my favorite!
            A[j] = tmp
        else:
            tmp = A[i-1]
            A[i-1] = A[0]
            A[0] =tmp
        permutation_generator(i-1, A)

st = "123"
st = list(st)
permutation_generator(len(st), st)
