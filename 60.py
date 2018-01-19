#60th prb
nterms=int(input())
n1 = 0
n2 = 1
count = 0
l=[]
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    l.append(n1)
    print(l)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        l.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print(l)
