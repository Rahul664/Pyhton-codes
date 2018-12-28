for _ in range(int(input())):
    i=int(input())
    cnt=0
    for cnt in range(100):
        if i%10==0:
            print(cnt)
            break
        else:
            i *= 2
            cnt += 1
        if cnt>=100:
            print(-1)
            break
