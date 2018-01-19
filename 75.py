#75th problem
s=input()
if(len(s)%2==0):
    s=s[:int((len(s)/2))-1]+'**'+s[int(len(s)/2)+1:]
else:
    s=s[:int(len(s)/2)]+'*'+s[int(len(s)/2)+1:]
print(s)
