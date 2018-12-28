def maximumProgramValue(n):
    temp = 0
    x = 0
    for i in range(n):
        op,y=map(str,input().split())
        y=int(y)
        if op=='add' and y>=0 and temp>=x:
            x+=y
            temp=x
        elif temp<=y:
            x=y
            temp=x
    return (x)
n=int(input())
result=maximumProgramValue(n)
print(result)