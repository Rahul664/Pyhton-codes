for _ in range(int(input())):
    x,y,z=map(int,input().split())
    cnt=0
    if x+y>z and y+z>x and z+x>y:
        if x==y==z:
            print("equilateral")
        elif x==y or y==z or z==x:
            print("isosceles")
            cnt+=1
        else:
            print("scalene")
    else:
        print("not triangle")

print(cnt)