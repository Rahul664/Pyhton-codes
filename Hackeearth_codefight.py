n=int(input())
eve=[]
od=[]
evesum=0
evesumarr=[]
odsumarr=[]
odsum=0
p=list(map(int,input().split()[:n]))
for i in range(0,n):
    if p[i]%2==0:
        eve.append(p[i])
        evesum+=p[i]
    else:
        od.append(p[i])
        odsum+=p[i]
eve.sort()
od.sort()
evesumarr.append(evesum)
odsumarr.append(odsum)
res=eve+evesumarr+od+odsumarr
print(' '.join(map(str,res)))
