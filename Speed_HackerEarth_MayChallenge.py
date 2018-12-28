from math import sqrt
for _ in range(int(input())):
    h,x,z=map(int,input().split())
    t1=sqrt((2*h)/32)
    t2=x/z
    if t2<=t1:
        print("Rahul")
    else:
        print("Raj")