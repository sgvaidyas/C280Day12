def isoperCheck(s):
    oper = "+-/^*"
    closingbrac = ")]}"
    openingbrac = "([{"
    valid = True
    for i in range(len(s)):
        if i+1<len(s):
            if (s[i] in oper) and (s[i+1] in oper):
                valid = False
            elif(s[i].isalpha() and s[i+1].isalpha()):
                valid = False
            elif s[-1] in oper:
                valid = False
            elif(s[i] in closingbrac and s[i+1].isalpha()):
                valid = False
            elif(s[i] in oper and s[i+1] in closingbrac):
                valid = False
            elif (s[i].isalpha() and s[i+1] in openingbrac):
                valid = False
            if valid==False:
                return False
    return valid

s = input("Enter the string")
print(isoperCheck(s))
