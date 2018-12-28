ar=list(map(int,input().split()))
ar.sort()
size=len(ar)
mid=int(size/2)
ar[mid-1],ar[mid]=ar[mid],ar[mid-1]
print(' '.join(map(str,ar)))