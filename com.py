ll=input().strip().split(' ')
ll=sorted(ll)
ll=ll[::-1]
ll="".join(str(xx) for xx in ll)
ll=ll[::-1]
s=[]
for ii in range(len(ll)):
    if ii%3==0 and ii!=0:
        s.append(',')    
    s.append(ll[ii])
s=s[::-1]    
s="".join(str(xx) for xx in s)    
print(s)  
