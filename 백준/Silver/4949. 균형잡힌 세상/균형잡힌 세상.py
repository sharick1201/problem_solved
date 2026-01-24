def is_balanced(s):
    stack = []  # 스택 쓰자

    for char in s:
        if char == '(' or char == '[':
            stack.append(char)

        elif char == ')' or char == ']':
            # 스택이 비어있으면 불균형
            if not stack:
                return "no"

            # 스택에서 최상단 요소 꺼내고, 짝이 맞지 않으면 불균형
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']'):
                return "no"

    return "yes" if not stack else "no"

while True:
    txt = input()
    if txt == '.':
        break

    print(is_balanced(txt))