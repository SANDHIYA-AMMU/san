#56th
n=input()
c=0
d=0
for char in n:
    if(char.isdigit()):
        c=c+1
    if(char.isalpha()):
        d=d+1
    if(c>0 and d>0):
        print('yes')
        break
if(c==0 or d==0):
        print('No')
