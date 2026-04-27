from collections import deque
from itertools import permutations, product
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        m = int(input())
        graph = [[] for _ in range(n + 1)]
        all_w_one = True
        for _ in range(m):
            u, v, w = int(input()), int(input()), int(input())
            if w != 1:
                all_w_one = False
            graph[u].append([v, w])
            graph[v].append([u, w])
        if all(len(i) == n - 1 for i in graph[1:]):
            # complete graph
            for j in graph[1]:
                answers.append(j[1])
        elif all_w_one:
            # simple bfs will do the trick.
            visited = [False for _ in range(n + 1)]
            length = [0 for _ in range(n + 1)]
            queue = deque([1])
            visited[1] = True
            ans = 0
            while queue:
                u = queue.popleft()
                for v, w in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        length[v] = length[u] + 1
            for i in range(2, n + 1):
                answers.append(length[i])
        elif n <= 10 and m <= 20:
            # smaller case, do some brute forcing.
            found_answer = [True, True] + [False for _ in range(n - 1)]
            path_sum = [0 for _ in range(n + 1)]
            path_count = [0 for _ in range(n + 1)]
            for i in range(2, n + 1):
                for j in permutations(range(1, n + 1), r=i - 1):
                    if found_answer[j[-1]]:
                        continue
                    pairs = []
                    for j1, j2 in zip([1] + list(j), j):
                        ws = [w[1] for w in graph[j1] if w[0] == j2]
                        if not ws:
                            pairs.clear()
                            break
                        pairs.append(ws)
                    if not pairs:
                        continue
                    for ws in product(*pairs):
                        path_sum[j[-1]] += sum(ws)
                    length = 1
                    for ws in pairs:
                        length *= len(ws)
                    path_count[j[-1]] += length
                for k in range(2, n + 1):
                    if path_count[k] == 0:
                        continue
                    found_answer[k] = True
            for i in range(2, n + 1):
                answers.append(path_sum[i] * pow(path_count[i], -1, MOD) % MOD)
    print(*answers, sep="\n")