# 1935 후위 표기식2
from sys import stdin

N = int(input())
formula = input()
numbers = [int(stdin.readline().rstrip()) for _ in range(N)]
operations = ["+", "-", "*", "/"]
stack = []

for i in formula:
    if i in operations:
        b_sub, a_sub = stack.pop(), stack.pop()
        if i == "+":
            stack.append(a_sub+b_sub)
        elif i == "-":
            stack.append(a_sub-b_sub)
        elif i == "*":
            stack.append(a_sub*b_sub)
        else:
            stack.append(a_sub/b_sub)
    else:
        stack.append(numbers[ord(i)-ord("A")])

print(f"{stack[0]:.2f}")