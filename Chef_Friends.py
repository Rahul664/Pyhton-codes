t=int(input())
cnt=0
while t:
    pattern1="ch"
    pattern2="ef"
    pattern3="he"
    s=input()
    size=len(s)
    while size:
        a=s.find(pattern1)
        if not(a==-1):
            cnt+=1
            break
        b=s.find(pattern2)
        if not(b==-1):
            cnt += 1
            break
        c=s.find(pattern3)
        if not(c==-1):
            cnt += 1
            break
        else:
            cnt
        size-=1
    t=t-1
print(cnt) 