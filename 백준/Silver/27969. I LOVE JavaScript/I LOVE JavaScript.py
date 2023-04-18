# K번

ason_object = list(input().split(" "))
bracket_stack = []
answer = 0
for i in ason_object:
    if i == "[":
        bracket_stack.append(1)
    elif i == "]":
        bracket_stack.pop()
        answer += 8
    elif i.isdigit():
        answer += 8
    else:
        answer += len(i) + 12
print(answer)