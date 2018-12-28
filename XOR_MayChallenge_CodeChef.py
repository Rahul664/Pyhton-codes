for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    res=0
    for i in range(len(a)):
        c=a[i]*2
        res^=(c)
    print(res)
