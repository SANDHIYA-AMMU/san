import math
def primeFactors(n):
    while n % 2 == 0:
        l.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            l.append(i)
            n = n / i
    if n > 2:
        l.append(n)
    return(l)
num = int(input())
l=[]
l=primeFactors(num)
l=set(l)
print(" ".join(str(x) for x in l))
