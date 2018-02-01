st1,st2=input().split(' ')
c=0
for i in range(len(st1)):
    if st1[i]!=st2[i]:
        c=c+1
if(c==1):print('yes')
else:print('no')
