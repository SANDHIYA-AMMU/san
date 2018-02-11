#69th prb
n,k=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
print(*l[:n-k])
