s1,s2=input().split(' ')
c=0
for i in s1:
    if i in s2:
        print('Yes')
        c+=1
        break
if c==0:print('No')
