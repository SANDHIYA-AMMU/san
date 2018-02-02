wor=list(input())
for i in range(len(wor)):
    if wor[i].islower():
        wor[i]=wor[i].upper()
    else:
        wor[i]=wor[i].lower()
print("".join(str(x) for x in wor))
