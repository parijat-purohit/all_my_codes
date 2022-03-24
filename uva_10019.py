"""
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=960
"""
t = int(input())
while(t):
    n = input()
    b1 = str(bin(int(n, base=10)))[2:].count('1')
    b2 = str(bin(int(n, base=16)))[2:].count('1')
    print(b1,b2)
    t-=1
