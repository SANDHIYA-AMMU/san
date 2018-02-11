#64th prb
n,k=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
s=[]
for i in l:
    if i<k:
        s.append(i)
print(*sorted(s))
