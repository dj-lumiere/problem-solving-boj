from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from itertools import product
from math import ceil, log2, atan2, pi, sqrt, cos, sin
from sys import stdout, stderr


class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1


def find_mst_cost(graph, V):
    edges = []
    for start in range(V):
        for end, cost in graph[start]:
            edges.append((cost, start, end))
    edges.sort()
    uf = UnionFind(len(graph))
    mst_cost = 0
    for edge in edges:
        cost, start, end = edge
        if uf.find(start) != uf.find(end):
            mst_cost += cost
            uf.union(start, end)
    return mst_cost


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
    t = int(input())
    answers = []
    for hh in range(t):
        n, m = int(input()), int(input())
        graph = [[] for _ in range(n)]
        answer = 0
        for i in range(1, n):
            u, c = (int(input()) for _ in range(2))
            graph[i].append((u, c))
        for _ in range(m):
            u, v, c = (int(input()) for _ in range(3))
            graph[u].append((v, c))
            answer ^= find_mst_cost(graph, n)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
