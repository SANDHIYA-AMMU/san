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



