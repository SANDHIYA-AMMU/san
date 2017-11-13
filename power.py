v=int(input())
c=0
while(v%2!=0):
    if v*(v-1)!=0 and (v-1)%2==0:
        v=v-1
        c=c+1
print(c)
    
