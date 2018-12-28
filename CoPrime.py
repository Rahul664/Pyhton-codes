def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
n=int(input())
l=list(map(int,input().split()[:n]))
cnt=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if j>i:
            for k in range(j+1,len(l)):
                if k>j:
                    if (gcd(l[i],gcd(l[j],l[k])))==1:
                        cnt+=1
print(cnt)