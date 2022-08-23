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
        print("Stack underflow")
        return None
    else:
        print("deleting .... = ",a[top])
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
string = "(4(444{(4444)44})444)"
balanced = True

for x in range(len(string)):
    if string[x] in openingBrackets:
        push(string[x])
    elif string[x] in closingBrackets:
        if pop() != closingBrackets[string[x]]:
            balanced = False
            break

if top != -1 or not balanced:
    print("Unbalanced")
elif balanced:
    print("Balanced")
