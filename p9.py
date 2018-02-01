low,upp=map(int,input().split(' '))
ll=list(1 for i in range(upp+1))
c=0
for i in range(2,upp+1,1):
    if ll[i]==1:
        for j in range(i*i,upp+1,i):
            ll[j]=0
        if i>=low:
            c+=1
print(c)
