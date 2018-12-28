def averageOfTopEmployees(rating):
    s=0
    cnt=0
    for i in rating:
        if i>=90:
            s+=i
            cnt+=1
    res=round(s/cnt,3)*1000
    if (int(res)%10)>=5:
        res=(int(res/10)+1)/100
        print('%.2f'%(res))
    else:
        print('%.2f'%(res/1000))

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
