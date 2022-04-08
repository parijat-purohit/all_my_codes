def LIS(i, A):
    if res[i]!=-1:
        return res[i]
    ans = 0
    j = i+1
    while(j<len(arr)):
        if arr[j] > arr[i]:
            ans = max(ans, LIS(j, arr))
        j=j+1
    res[i] = 1 + ans
    return res[i]

arr = [100,9,8,7,6,30,20,56,63]

ans = 0
maxim = 0
path = []
for n in range(len(arr)):
    res = [-1] * 20
    ans = max(ans, LIS(n, arr))
    if ans>maxim:
        maxim = ans
        path = res

print(ans)
# path printing
for i in range(len(arr)):
    if path[i] > path[i+1]:
        print(arr[i])
