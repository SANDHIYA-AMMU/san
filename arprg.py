n,a,d=input("Enter n, a and d").split(' ')
n,a,d=int(n),int(a),int(d)
ans=0
total=0
while n>=0:
    total+=ans
    ans+=d
    n-=1
print(total)
