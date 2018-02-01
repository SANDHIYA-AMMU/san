def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    if(list_str1 == list_str2):
        return('1')
    else:
        return('0')

n=int(input())
l=[]
for i in range(n):
    l.append(input())
s='kabali'
c=0
for j in range(n):
    if(is_anagram(s,l[j]) == '1'):
        c=c+1
print(c)
