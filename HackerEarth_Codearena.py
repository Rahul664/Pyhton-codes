from numpy import unique
n=int(input())
a=[int(input()) for i in range(n)]
b=unique(a)
if len(b)==2 and a.count(b[0])==a.count(b[1]):
    print("YES")
    print(' '.join(map(str,b)))
else:
    print("NO")

