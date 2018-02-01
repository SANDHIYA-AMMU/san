def roman(s):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    inc = 0
    for i in range(len(s)):
        if i > 0 and val[s[i]] > val[s[i - 1]]:
                inc += val[s[i]] - 2 * val[s[i - 1]]
        else:
                inc += val[s[i]]
    return inc
string = input("Enter the roman no")
print(roman(string))
