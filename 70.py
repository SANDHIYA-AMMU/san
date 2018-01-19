n=int(input())
if n == 0:
    print(1)
if n & (n - 1) == 0:
    print(n)
while n & (n - 1) > 0:
    n &= (n - 1)
print(n << 1)
 
