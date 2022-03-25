"""
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1012
"""
while True:
        try:
            inp = input()
            st = inp.split(' ')
            print(2*int(st[0])*int(st[1]))
        except:
            break
