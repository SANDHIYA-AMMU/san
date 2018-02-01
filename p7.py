ll=list(input())
for i in range(0,len(ll)-1,2):
    ll[i],ll[i+1]=ll[i+1],ll[i]
print("".join(str(x) for x in ll))

#8th prb
str=input()
print(str.title())
