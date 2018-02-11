#68th prb
num=int(input('Enter n:'))
l1,c,maxi=[],0,-1
print('Enter elements :')
for i in range(num):
    l1.append(int(input()))
for i in range(num):
    for j in range(i+1,num):
        if l1[i]==l1[j]:
            c+=1
    if maxi<c:
        maxi=c
    c=0
print(maxi+1)
