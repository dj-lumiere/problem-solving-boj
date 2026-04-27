import os
from collections import Counter

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        reachable = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        worldmap = input().decode()
        for j, v in enumerate(worldmap):
            if v == "E":
                graph[j].append(j + 1)
            if v == "W":
                graph[j].append(j - 1)
        current_group = 0
        for j in range(n):
            if reachable[j] != 0:
                continue
            current_group += 1
            reachable[j] = current_group
            stack = []
            stack.append(j)
            while stack:
                current = stack.pop()
                for future in graph[current]:
                    if reachable[future] != 0:
                        reachable[current] = reachable[future]
                        continue
                    reachable[future] = reachable[current]
                    stack.append(future)
        answer = len(Counter(reachable).keys())
        answers[i] = f"{answer}"
    print(answers)