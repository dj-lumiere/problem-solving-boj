from collections import deque
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N, M = int(input()), int(input())
        graph = [[] for _ in range(N + 1)]
        for _ in range(M):
            x, y = int(input()), int(input())
            graph[x].append(y)
        queue = deque([(1, 0)])
        visited = [False] * (N + 1)
        visited[1] = True
        answer = -1
        while queue:
            current_node, step_count = queue.popleft()
            if current_node == N:
                answer = step_count
                break
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, step_count + 1))
        answers.append(f"{answer}")
    print(*answers, sep="\n")