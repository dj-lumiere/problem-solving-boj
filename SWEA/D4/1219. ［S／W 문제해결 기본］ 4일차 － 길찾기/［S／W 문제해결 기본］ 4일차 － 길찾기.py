from itertools import product
from math import log2, ceil

t = 10
answers = []
for hh in range(t):
    a, r = map(int, input().split())
    graph = [[] for _ in range(100)]
    stack = [0]
    visited = [False for _ in range(100)]
    visited[0] = True
    roads = list(map(int, input().split()))
    for x, y in zip(roads[::2], roads[1::2]):
        graph[x].append(y)
    while stack:
        x = stack.pop()
        for nx in graph[x]:
            if visited[nx]:
                continue
            visited[nx] = True
            stack.append(nx)
    answer = int(visited[99])
    answers.append(f"#{a} {answer}")
print(*answers, sep="\n")
