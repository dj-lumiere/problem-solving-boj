# 4386 별자리 만들기

from sys import stdin


def input():
    return stdin.readline().strip()


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


N = int(input())
graph = [[] for _ in range(N)]
node = []
for i in range(N):
    x, y = map(float, input().split(" "))
    node.append((x, y))
for i, (x1, y1) in enumerate(node):
    for j, (x2, y2) in enumerate(node):
        if i == j:
            continue
        graph[i].append((j, ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))

print(find_mst_cost(graph, N))