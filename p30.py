lis1,lis2,k1=input().split(' ')
k1=int(k1)
c=0
for i in range(len(lis1)):
    if lis1[i]!=lis2[i]:
        c+=1
if c==k1:print("yes")
else:print("no")
