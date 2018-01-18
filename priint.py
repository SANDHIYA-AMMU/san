n,k=input().split(' ')
n,k=int(n),int(k)
for num in range(n+1,k):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
           else:
               print(num)
