import os
from collections import Counter, deque
from itertools import product
from array import array
from functools import reduce

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        node = [int(input()) for _ in range(n)]
        graph = [[] for _ in range(n + 1)]
        for i, v in enumerate(node, start=1):
            graph[i].append(v)
        group = [0 for _ in range(n + 1)]
        current_group_number = 0
        for i in range(1, n + 1):
            if group[i] != 0:
                continue
            current_group_number += 1
            stack = [i]
            group[i] = current_group_number
            while stack:
                current = stack.pop()
                for now in graph[current]:
                    if group[now] != 0:
                        continue
                    stack.append(now)
                    group[now] = current_group_number
        answer = max(group)
        answers[h] = f"{answer}"
    print(answers)