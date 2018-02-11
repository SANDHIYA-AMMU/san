#67th prb
def fact(s):
    if s==1 or s==0:
        return 1
    else:
        return s*fact(s-1)
print(fact(int(input())))
