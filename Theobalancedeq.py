def task1():
    push_brackets = ("(", "{", "[",)
    pop_brackets = (")", "}", "]",)
    equation = "([a+b]-(d/c))"
    stack = []
    balanced = 1
    for w in equation:
        if w in push_brackets:
            stack.append(w)
        if w in pop_brackets:
            if len(stack) < 1:
                balanced = 0
                break
            j = stack.pop()
            if w == ")":
                reverse = "("
            elif w == "}":
                reverse = "{"
            elif w == "]":
                reverse = "["
            if j != reverse:
                balanced = 0
                break
    if len(stack) > 0:
        balanced = 0
    print("Equation: " + equation)
    if balanced == 1:
        print("\033[1;32mEquation is balanced!")
    else:
        print("\033[1;31mEquation is NOT balanced!")

if __name__ == '__main__':
    task1()
