def push(ele):
    global top
    if top==max-1:
        print("Stack overflow")
    else:
        top+=1
        a[top]=ele

def pop():
    global top
    if top==-1:
        return None
    else:
        top-=1
    return a[top+1]

def display():
    global top
    if top==-1:
        print("Stack is empty")
    else:
        print("Elements of stack are = ")
        for i in range(top,-1,-1):
            print(a[i])

def peek():
    global top
    print("-------------------------------")
    print("Top most element = ",a[top])
    print("-------------------------------")

max = 10
a = [0]*max
top=-1

openingBrackets = {"(", "[", "{"}
closingBrackets = {")": "(", "]": "[", "}": "{"}
symbols = {"+", "-", "/", "*", "^"}
string = "(a+b-(4/3)*{1+2})"
string = "-(a+b-(4/3)*{1+2})"
string = "(a+b-(4/3)*{1+2})-"
#string = "(a+b-4/3)*{1+2})"
balanced = True
justOperated = False


for x in range(len(string)):
    print(x)
    print(string[x])

    if x == len(string)-1 and string[x] in symbols:
        balanced = False
        break

    elif string[x] in openingBrackets:
        push(string[x])
        justOperated = False

    elif string[x] in closingBrackets:
        if justOperated:
            balanced = False
            break
        removed = pop()
        justOperated = False
        if removed != closingBrackets[string[x]]:
            balanced = False
            break

    elif string[x] in symbols and justOperated:
        balanced = False
        break

    elif string[x] in symbols and not justOperated:
        justOperated = True

    elif string[x] not in symbols:
        justOperated = False

if top != -1 or not balanced:
    print("Invalid")
elif balanced:
    print("Valid")
