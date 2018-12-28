t=int(input())
while t:
    s = input()
    sum1=0
    n=len(s)
    for c in s:
        if c.isdigit():
            sum1+=int(c)
    print(sum1)
    t=t-1