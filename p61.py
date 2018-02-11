#61th prb
n,k=map(int,input().split(' '))
c=0
arr=list(map(int,input().split(' ')))
for i in range(0, n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == k:
                c+=1
                print('yes')
                break
if(c==0):print('no')
