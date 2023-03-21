# 4949 균형잡힌 세상


def right_bracket(string_to_check: list[str]) -> str:
    bracket_stack: list[int] = []
    for i in string_to_check:
        if i == "(":
            bracket_stack.append(1)
        elif i == "[":
            bracket_stack.append(2)
        elif i == ")" and (not bracket_stack or bracket_stack[-1] != 1):
            bracket_stack.append(-1)
        elif i == ")" and bracket_stack and bracket_stack[-1] == 1:
            bracket_stack.pop()
        elif i == "]" and (not bracket_stack or bracket_stack[-1] != 2):
            bracket_stack.append(-2)
        elif i == "]" and bracket_stack and bracket_stack[-1] == 2:
            bracket_stack.pop()
    if bracket_stack:
        return "no"
    else:
        return "yes"


while True:
    right_bracket_check = list(input().rstrip("."))
    if right_bracket_check:
        print(right_bracket(right_bracket_check))
    else:
        break
