# 1197 최소 스패닝 트리

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
    for start in range(1, V + 1):
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


V, E = map(int, input().split(" "))
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end, cost = map(int, input().split(" "))
    graph[start].append((end, cost))
    graph[end].append((start, cost))

print(find_mst_cost(graph, V))