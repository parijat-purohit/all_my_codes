"""
binary search in a sorted array O(logN)
"""
def binary_search(array, key):
    begin = 0
    end = len(array) -1
    index = None
    while(begin<=end):
        mid = int((begin+end)/2)
        if key==array[mid]:
            index = mid
            break
        elif key>array[mid]:
            begin = mid + 1
        elif key<array[mid]:
            end = mid - 1
    return index

a = [1,2,3,4,5,6,7,8,9]
print(binary_search(a,2))
