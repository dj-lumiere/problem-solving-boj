# 1662 압축

S = list(input())
stack = []
multiplier = []
for i, v in enumerate(S):
    if not stack and v not in ("(", ")"):
        stack.append(0)
    if stack and v not in ("(", ")"):
        stack[-1] += 1
    if stack and v == "(":
        stack[-1] -= 1
        stack.append(0)
        multiplier.append(int(S[i - 1]))
    if stack and v == ")":
        stack[-1] *= multiplier.pop()
        latest_parenthesis_length = stack.pop()
        stack[-1] += latest_parenthesis_length
print(stack[0])