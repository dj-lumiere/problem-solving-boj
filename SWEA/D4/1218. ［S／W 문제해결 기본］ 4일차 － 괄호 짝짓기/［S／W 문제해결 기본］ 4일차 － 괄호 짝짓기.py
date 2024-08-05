from itertools import product
from math import log2, ceil

t = 10
answers = []
for hh in range(t):
    _ = int(input())
    s = input()
    stack = []
    is_answer = True
    for v in s:
        if not stack:
            stack.append(v)
            continue
        if v in "({[<":
            stack.append(v)
            continue
        if stack[-1] == "(" and v == ")":
            stack.pop()
            continue
        if stack[-1] == "{" and v == "}":
            stack.pop()
            continue
        if stack[-1] == "[" and v == "]":
            stack.pop()
            continue
        if stack[-1] == "<" and v == ">":
            stack.pop()
            continue
        stack.append(v)
    if stack:
        is_answer = False
    answer = int(is_answer)
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")