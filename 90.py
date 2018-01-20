#90th prb
l=list(input())
k=[]
for x in l:
    if x.isdigit():
        k.append(x)
print("".join(str(n) for n in k))
