for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()[:n]))
    msumm = tsumm = 0
    for j in range(k):
        maxi = 0
        mini = 10001
        for i in range(len(a)):
            if i%2==0 and a[i]>maxi:
                maxi=a[i]
                maxii=i
            elif i%2!=0 and a[i]<mini:
                mini=a[i]
                minii=i
        if maxi>mini:
            a[maxii],a[minii]=a[minii],a[maxii]
    for i in range(len(a)):
        if i%2==0:
            msumm+=a[i]
        else:
            tsumm+=a[i]
    if tsumm>msumm:
        print("YES")
    else:
        print("NO")