num=int(input("Enter the N value:"))
p1=[]
p2=[]
for x in range(num):
	l=input()
	p1.append(l)
for x in p1:
	for y in x:
		if y!=' ':
			p2.append(y)
print(min(p2))

#38 problem
v=int(input())
l=[]
for i in range(2,v+1,2):
    if v%i==0:
        l.append(i)
print(" ".join (str(i) for i in l))
