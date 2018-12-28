from itertools import combinations

t=int(input())
while t:
    n =int(input())
    cnt =0
    a=list(map(int,input().split()[:n]))
    b=set([i<<1 for i in a])
    c=list(sum(x) for x in combinations(a,2))
    for i in c:
        if i in b:
            cnt+=1
    print(cnt)
    t=t-1
'''
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    Ad = Counter(A)

    B = list(Ad.keys())
    BF = list(Ad.values())
    BS = set([b << 1 for b in B])
    print(BS)
    otpt, m = 0, len(B)
    for i in range(m):
        a0, a1f = B[i], BF[i]
        otpt += (a1f * (a1f - 1)) >> 1
        for j in range(i + 1, m):
            a1 = a0 + B[j]
            if a1 in BS: otpt += (a1f * BF[j])
    print(otpt)'''