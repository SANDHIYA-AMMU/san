#114th prb
n,k=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
s=[]
for x in l:
    if(x%2!=0):
        s.append(x)
print(s[k-1])
