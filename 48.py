#48th prb
l=list(map(int,input().split()))
sum=0
for x in l:
    sum=sum+x
print(int(sum/len(l)))
