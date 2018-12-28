from collections import Counter
t=int(input())
while t:
    n,k=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    l=Counter(a)
    s=-1
    c=0
    for i,j in l.items():
        if l[i]==k:
            c=1
            s+=i
    if c==1:
        print(s+1)
    else:
        print(s)
    t=t-1