# printing the square of numbers using a function
# 4 lines
def squared(num):
    return num*num
l1 = [1,2,3,4,5]
print(list(map(squared, l1)))

# using lambda would make this code even shorter
# by getting rid of the function
# 2 lines
l2 = [1,2,3,4,5]
print(list(map(lambda x: x*x, l2)))
