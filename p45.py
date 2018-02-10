#45th prb
p=list(map(int,input().split(' ')))
s=int(p[1]**0.5)
if float(s)==float(p[1]**0.5):
    if int(p[1]**(0.5))==(p[0]//4):
        print('Yes')
    else:
        print('No')
else: print('No')
