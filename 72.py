vowel=['a','e','i','o','u','A','E','I','O','U']
def vw(string):
    for i in vowel:
        if i in string:
            return "yes"
    return "no"
string=list(input("Enter the string"))
print(vw(string))
