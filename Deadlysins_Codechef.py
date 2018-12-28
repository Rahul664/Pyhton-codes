from math import gcd
t=int(input())
while t:
    c = list(map(int, input().split()))
    x=c[0]
    y=c[1]
    g=gcd(x,y)
    if x==y:
        print(x+y)
    else:
        print(g*2)
    t=t-1

