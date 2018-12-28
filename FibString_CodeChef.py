from collections import Counter

for _ in range(int(input())):
    a=input()
    c=Counter(a)
    if len(c)<3:
        print("Dynamic")
    else:
        p=[]
        per=[]
        cnt=0
        for i,j in c.items():
            p.append(c[i])
        per=sorted(p)
        for i in range(len(per)-1,1,-1):
            if per[i]==per[i-1]+per[i-2]:
                cnt=1
        if cnt==1:
            print("Dynamic")
        else:
            print("Not")