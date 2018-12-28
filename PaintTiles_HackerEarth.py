n=int(input())
s=input()
begin=s[0]
cnt=0
for i in s:
    if begin!=i:
        begin=i
        cnt+=1
print(cnt+1)