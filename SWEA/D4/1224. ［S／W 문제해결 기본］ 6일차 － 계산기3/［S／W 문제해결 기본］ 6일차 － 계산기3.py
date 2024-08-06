def operator_process_order(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0


def evaluate(expression):
    stack = []
    post_expression = ""
    for i, v in enumerate(expression):
        if "0" <= v <= "9":
            post_expression += v
            continue
        if v == "(":
            stack.append(v)
        elif v == ")" and stack[-1] == "(":
            stack.pop()
        elif v == ")" and stack[-1] != "(":
            while stack and stack[-1] != "(":
                post_expression += stack.pop()
            if stack and stack[-1] == "(":
                stack.pop()
        else:
            while stack and stack[-1] != "(" and operator_process_order(stack[-1]) >= operator_process_order(v):
                post_expression += stack.pop()
            stack.append(v)
    stack = []
    for i, v in enumerate(post_expression):
        if "0" <= v <= "9":
            stack.append(int(v))
            continue
        if v == "+":
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif v == "*":
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
    return stack[0]


t = 10
answers = []
for hh in range(t):
    n = int(input())
    expression = input()
    answer = evaluate(expression)
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")
