a,b=map(int,input("Enter two value").split(' '))
ll=[]
for i in range(1,int(max([a,b])/2)+2,1):
    if a%i==0 and b%i==0:
        ll.append(i)
if len(ll)==1:print("1")
else:print(max(ll))
