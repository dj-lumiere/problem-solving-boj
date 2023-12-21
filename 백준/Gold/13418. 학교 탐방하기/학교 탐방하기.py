# 13418 학교 탐방하기


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
    for start, a in enumerate(graph):
        for end, cost in a:
            edges.append((cost, start, end))
    edges.sort()

    uf = UnionFind(len(graph))
    mst = []

    for edge in edges:
        cost, start, end = edge
        if uf.find(start) != uf.find(end):
            mst.append(edge)
            uf.union(start, end)

    return mst


N, M = map(int, input().split(" "))
only_uphill_graph = [[] for _ in range(N + 1)]
all_node_graph = [[] for _ in range(N + 1)]
for _ in range(M + 1):
    A, B, C = map(int, input().split(" "))
    if C == 0:
        only_uphill_graph[A].append((B, 1))
    all_node_graph[A].append((B, 1 - C))

mst_only_uphill = kruskal(only_uphill_graph)
mst_all_node = kruskal(all_node_graph)
print(sum(i[0] for i in mst_only_uphill) ** 2 - sum(i[0] for i in mst_all_node) ** 2)
