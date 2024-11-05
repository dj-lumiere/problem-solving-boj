from collections import deque
from heapq import heappop, heappush
from itertools import product, permutations
from sys import stderr, stdout


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


def kruskal(N, edges):
    uf = UnionFind(N)
    mst = []
    min_cost = 0
    for edge in edges:
        w, u, v = edge
        if uf.find(u) != uf.find(v):
            mst.append(edge)
            min_cost += w
            uf.union(u, v)
    return mst, min_cost


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        n = int(input())
        points = [(i, int(input()), int(input()), int(input())) for i in range(n)]
        edges = []
        points.sort(key=lambda x: x[1])
        for (i1, x1, y1, z1), (i2, x2, y2, z2) in zip(points, points[1:]):
            dist_sub = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
            edges.append((dist_sub, i1, i2))
        points.sort(key=lambda x: x[2])
        for (i1, x1, y1, z1), (i2, x2, y2, z2) in zip(points, points[1:]):
            dist_sub = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
            edges.append((dist_sub, i1, i2))
        points.sort(key=lambda x: x[3])
        for (i1, x1, y1, z1), (i2, x2, y2, z2) in zip(points, points[1:]):
            dist_sub = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
            edges.append((dist_sub, i1, i2))
        edges.sort()
        _, answer = kruskal(n, edges)
        answers.append(answer)
    print(*answers, sep="\n")
