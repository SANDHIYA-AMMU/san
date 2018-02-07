#50th prb
num = int(input())
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("Yes")
           break
       else:
           print("N0")
else:
   print("Yes")
