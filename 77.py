#77th problem
x=int(input())
l=[]
for i in range(1, x + 1):
       if x % i == 0:
           l.append(i)
print(" ".join(str(n) for n in l))
