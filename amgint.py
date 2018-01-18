lo,up=input().split()
lo,up=int(lo),int(up)
l=[]
for num in range(lo+1, up ):

   order = len(str(num))

   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       l.append(num)
print(" ".join(str(x) for x in l))
