from itertools import combinations


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

INF = 10 ** 18
MOD = 1_000_000_000
t = int(input())
answers = []
for hh in range(1, t + 1):
    v = int(input())
    x_coordinates = list(map(int, input().split()))
    y_coordinates = list(map(int, input().split()))
    e = float(input())
    graph = [[] for _ in range(v + 1)]
    for (i, (x1, y1)), (j, (x2, y2)) in combinations(enumerate(zip(x_coordinates, y_coordinates), start=1), r=2):
        graph[i].append((j, ((x1 - x2) ** 2 + (y1 - y2) ** 2) * e))
        graph[j].append((i, ((x1 - x2) ** 2 + (y1 - y2) ** 2) * e))
    answer = f"{find_mst_cost(graph, v):.0f}"
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")
