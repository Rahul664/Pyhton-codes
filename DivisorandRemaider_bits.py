t=int(input())
while t:
    a=int(input())
    cnt=0
    for i in range(1,a+1):
        if (bin(int(a/i))<=bin(int(i))):
            cnt+=1
            cnt=cnt%1000000007
    print(cnt)
    t=t-1