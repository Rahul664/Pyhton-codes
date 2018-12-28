def dynamicLineIntersection(n):
    c=d=y=k=b=x=q=0
    pst=[]
    ngt=[]
    ques=[]
    for i in range(n):
        args=input()
        if len(args)==5:
            if args[0]=='+':
                c,d=int(args[2]),int(args[4])
                pst.append([c,d])
            else:
                c,d=int(args[2]),int(args[4])
                ngt.append([c,d])
        else:
            q=int(args[2])
            if len(ngt)!=0:
                for i in range(len(ngt)):
                    if ngt[i] in pst:
                        pst.remove(ngt[i])
            if len(pst)!=0:
                cnt=0
                for i in range(len(pst)):
                    if q!=0:
                        b=pst[i][1]
                        k=pst[i][0]
                        if (q-b)%k==0:
                            cnt+=1
                print(cnt)
if __name__ == '__main__':
    n = int(input())

    dynamicLineIntersection(n)