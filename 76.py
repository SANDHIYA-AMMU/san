#76th problem
n=int(input())
factor=0
for i in range(1,n):
  if n%i==0:
    factor=i
if factor>1:
  print ('Yes')
elif n==1:
  print ('neither prime nor composite')
else:
  print ('No')
