n=int(input())
l=[]
for i in range(1,6,1):
    l.append(n*i)
print(" ".join(str(x) for x in l))
