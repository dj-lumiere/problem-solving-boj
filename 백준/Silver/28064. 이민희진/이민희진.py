# 28064 이민희진

from itertools import combinations
from sys import stdin, stdout

# stdin = open("test_input.txt", "r")
# stdout = open("test_output.txt", "w")

input = stdin.readline
print = stdout.write

N = int(input().strip())
names = [input().strip() for _ in range(N)]
answer = 0

for target1, target2 in combinations(names, 2):
    is_answer = False
    for index, value in enumerate(target1):
        if target2.startswith(target1[-index - 1 :]):
            answer += 1
            is_answer = True
            break
    if not is_answer:
        for index, value in enumerate(target2):
            if target1.startswith(target2[-index - 1 :]):
                answer += 1
                break
print(f"{answer}\n")