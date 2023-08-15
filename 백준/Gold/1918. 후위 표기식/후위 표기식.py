# 1918 후위 표기식


def get_operation_priority(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    return 0


expression = list(input())
stack = []
result = ""
parenthesis_stack = 0
for i, v in enumerate(expression):
    if "A" <= v <= "Z":
        result += v
    elif v == "(":
        stack.append(v)
    elif v == ")":
        while stack and stack[-1] != "(":
            result += stack.pop()
        stack.pop()
    else:
        while (
            stack
            and stack[-1] != "("
            and get_operation_priority(stack[-1]) >= get_operation_priority(v)
        ):
            result += stack.pop()
        stack.append(v)
while stack:
    result += stack.pop()
print(result)