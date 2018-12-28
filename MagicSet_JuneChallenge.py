for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()[:n]))
    count = 0
    for i in range(n):
        for j in range(i, n):
            sm = 0
            in_count = 0
            for k in range(i, j+1):
                in_count += 1
                sm += a[k]
            if sm % m == 0:
                count += 1
    if sum(a)%m==0:
        count-=1
    print(count)

