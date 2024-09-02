from collections import deque, Counter
from itertools import product, chain, permutations
from sys import stdout, stderr
from time import perf_counter

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, k, t = (int(input()) for _ in range(3))
        k **= 2
        xp, yp, vp = (int(input()) for _ in range(3))
        nodes = [[xp, yp, vp]] + [[0, 0, 0] for _ in range(n)]
        photo_with_pooang = [False for _ in range(n + 1)]
        for i in range(1, n + 1):
            xi, yi, vi, pi = (int(input()) for _ in range(4))
            if pi == 1:
                photo_with_pooang[i] = True
            nodes[i] = [xi, yi, vi]
        graph = [[] for _ in range(n + 1)]
        for (i, (xi, yi, vi)), (j, (xj, yj, vj)) in permutations(enumerate(nodes), r=2):
            if (xi - xj) ** 2 + (yi - yj) ** 2 <= k and abs(vi - vj) <= t:
                graph[i].append(j)
                graph[j].append(i)
        visited = [False for _ in range(n + 1)]
        queue = deque([0])
        visited[0] = True
        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                queue.append(nxt)
        result = [i for i, (v1, v2) in enumerate(zip(visited, photo_with_pooang)) if v1 and v2 and i != 0]
        answer = " ".join(map(str, result)) if result else "0"
        answers.append(f"{answer}")
print(*answers, sep="\n")
