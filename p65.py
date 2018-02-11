#65th prb
n=int(input())
l=list(map(int,input().split(' ')))
s=[]
for i in l:
    if i<n:
        s.append(i)
print(*sorted(s))
