symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+1234567890"
name = input()
c=0
for i in name:
    if i in symbol:
        c=c+1
print(c)
