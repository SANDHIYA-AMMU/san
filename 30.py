#30th prb
h1,m1=input().split()
h1,m1=int(h1),int(m1)
h2,m2=input().split()
h2,m2=int(h2),int(m2)
l1=(h1*60)+m1
l2= (h2*60)+m2
total_min=abs(l1-l2)
min = total_min  % 60
hrs = (total_min - min) / 60
print (int(hrs),int(min))
