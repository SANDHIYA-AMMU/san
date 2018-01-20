#81 problem
n=int(input("Enter the number of lines"))
for i in range(n):
    a,b=map(int,input("Ninja's and kabali's value").split(' '))
    print(abs(a-b))
