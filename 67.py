#67th problem
import math
n=int(input("Enter Value"))
if n<10: print("10")
else:
    l=len(str(n))
    n+=5
    n=n/(10**(l-1))
    print(math.floor(n)*(10**(l-1)))
