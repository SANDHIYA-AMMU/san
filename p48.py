#48th prb
x=int(input())
l=[]
for i in range(1, x):
    if x % i == 0 and i%2!=0:
        l.append(i)
print(*l)
