#41th prb
n,k=map(int,input().split(' '))
while(n%k==0):
    n=n/k
if n==1:print('Yes')
else: print('No')
