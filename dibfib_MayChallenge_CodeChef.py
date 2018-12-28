T = int(input())
for t in range(T):
    lis = list(map(int, input().split()))
    m = lis[0]
    n = lis[1]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    p = 1000000007
    fiba = [0] * (n + 2)
    fiba[1] = 1
    fiba[2] = 0
    for i in range(3, n + 2):
        fiba[i] = fiba[i - 1] + fiba[i - 2]

    print(((fiba[n] * sum(a) + fiba[n + 1] * sum(b)) * m) % p)