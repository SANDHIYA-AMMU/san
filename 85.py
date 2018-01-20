#85 problem
s=input("Enter a string")
l1=[]
l2=[]
for i in range(len(s)):
    if i%2==0:l1.append(s[i])
    else:l2.append(s[i])
print("".join(str(x) for x in l1),"".join(str(x) for x in l2))
