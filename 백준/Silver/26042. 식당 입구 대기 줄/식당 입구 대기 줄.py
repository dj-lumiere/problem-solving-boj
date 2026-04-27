import os
from collections import deque
from copy import deepcopy

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        queue = deque()
        answer = [0, 10000000]
        for _ in range(n):
            op = int(input())
            if op == 1:
                queue.append(int(input()))
                if answer[0] == 0:
                    answer = [len(queue), queue[-1]]
                elif answer[0] < len(queue) or (answer[0] == len(queue) and queue[-1] < answer[-1]):
                    answer = [len(queue), queue[-1]]
            if op == 2:
                queue.popleft()
        answers[h] = f"{answer[0]} {answer[1]}"
    print(answers)