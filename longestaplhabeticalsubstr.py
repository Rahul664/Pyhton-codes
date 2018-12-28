
s=input("Enter the string")

temp=[]
maxsub=[]
for i in range(0,len(s)-1):
    if (s[i]<=s[i+1]):
           if temp==[]:
                temp.append(s[i])
                temp.append(s[i+1])
           else:
                temp.append(s[i+1])
                maxsub.append(temp)
    else:
       if temp == []:
        temp.append(s[i])
        print(temp)
       maxsub.append(temp)
       temp = []
lengths=[]
for j in maxsub:
    lengths.append(len(j))
print(temp)
print (lengths)
print (maxsub)
substr=''.join(maxsub[lengths.index(max(lengths))])
print('Longest substring in alphabetical order is:'+substr)