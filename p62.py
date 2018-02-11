#62nd prb
n=int(input())
c=0
for i in range(1,n+1):
    c=n/i
    if(c%2!=0):
        print(i)
        break
