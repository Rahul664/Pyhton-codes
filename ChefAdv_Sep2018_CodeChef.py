for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    flag=0
    a=n-1
    b=m-1
    if a>=0 and b>=0:
        if a%x==0 and b%y==0:
            flag=1
    a=a-1
    b=b-1
    if a>=0 and b>=0:
        if a%x==0 and b%y==0:
            flag=1

    if flag==1:
        print("Chefirnemo")
    else:
        print("Pofik")
