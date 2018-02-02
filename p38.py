v=int(input())
l=[]
for i in range(2,v+1,2):
    if v%i==0:
        l.append(i)
print(" ".join (str(i) for i in l))
