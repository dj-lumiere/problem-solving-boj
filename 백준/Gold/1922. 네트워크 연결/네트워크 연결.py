# 1922 네트워크 연결


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


def kruskal(graph):
    edges = []
    for i, u in enumerate(graph):
        for v, w in u:
            edges.append((w, i, v))
    edges.sort()

    uf = UnionFind(len(graph))
    mst = []
    min_cost = 0
    for edge in edges:
        w, u, v = edge
        if uf.find(u) != uf.find(v):
            mst.append(edge)
            min_cost += w
            uf.union(u, v)
    return mst, min_cost


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    graph[a].append((b, c))
    graph[b].append((a, c))
_, min_cost = kruskal(graph)
print(min_cost)
