st1,st2=input().split(' ')
c=0
d=0
if(len(st1)==len(st2)):
    for i in range(0,len(st1)-1,1):
        if(st1[i]==st1[i+1]):
            c=c+1
            print(c)
        if(st2[i]==st2[i+1]):
            d=d+1
        if(c!=d):
            print('no')
            break
    print(c>0,c,d)
    if c==d:print('yes')
else:print('no')
