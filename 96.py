#96th prb
num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Yes")
            break
    else:
        print("No")
elif num == 0 or 1:
    print(" a neither prime NOR composite number")
else:
    print("Yes")
