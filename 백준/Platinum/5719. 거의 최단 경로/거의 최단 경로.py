from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from itertools import product
from math import ceil, log2
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
    MOD = 1_000_000_007
    t = INF
    answers = []
    for hh in range(t):
        n, m = (int(input()) for _ in range(2))
        if n == m == 0:
            break

        s, d = (int(input()) for _ in range(2))
        parents = [set() for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = (int(input()) for _ in range(3))
            graph[u].append((v, w))

        distance = [INF for _ in range(n)]
        heap = []
        visited = set()
        heappush(heap, (0, s, -1))
        distance[s] = 0
        min_dist = INF
        while heap:
            cost, next_node, parent = heappop(heap)
            if distance[next_node] < cost:
                continue
            if next_node == d and cost > min_dist:
                heap.clear()
                break
            parents[next_node].add(parent)
            if next_node == d:
                min_dist = distance[d]
            for i, j in graph[next_node]:
                next_cost = cost + j
                if next_cost > distance[i]:
                    continue
                if (next_cost, i, next_node) in visited:
                    continue
                visited.add((next_cost, i, next_node))
                distance[i] = next_cost
                heappush(heap, (next_cost, i, next_node))
        parents[s].clear()
        heap.clear()

        remove_stack = [d]
        visited = [False for _ in range(n)]
        remove_requirements = set()
        visited[d] = True
        while remove_stack:
            start = remove_stack.pop()
            for end in parents[start]:
                remove_requirements.add((end, start))
                if end == s:
                    continue
                if visited[end]:
                    continue
                visited[end] = True
                remove_stack.append(end)

        distance = [INF for _ in range(n)]
        heappush(heap, (0, s))
        distance[s] = 0
        min_dist = INF
        while heap:
            cost, next_node = heappop(heap)
            if distance[next_node] < cost:
                continue
            if next_node == d:
                min_dist = distance[d]
                break
            for i, j in graph[next_node]:
                next_cost = cost + j
                if next_cost > distance[i]:
                    continue
                if (next_node, i) in remove_requirements:
                    continue
                distance[i] = next_cost
                heappush(heap, (next_cost, i))
        answer = min_dist if min_dist != INF else -1
        answers.append(f"{answer}")
    print(*answers, sep="\n")
