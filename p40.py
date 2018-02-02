num=int(input())
c=0
for x in range(num+1):
	for y in range(num+1):
		way=(x*1)+(y*2)
		if way==num:
			c+=1
print(c)
