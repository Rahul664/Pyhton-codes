from math import gcd

def gcd_func(g):
    result=g[0]
    for i in range(1,len(g)):
        result=gcd(result,g[i])
    return result

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    cnt=0
    res=gcd_func(a)
    while res!=1 and len(a)!=1:
        cnt+=1
        a.pop()
        res=gcd_func(a)
    if res==1:
        print(cnt)
    else:
        print(-1)
