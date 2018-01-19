#79th problem
import math
i,j=map(int,input().split(' '))
n=i*j
if math.sqrt(n)==int( math.sqrt(n)):
    print ("Yes")
else:
    print ("No")
