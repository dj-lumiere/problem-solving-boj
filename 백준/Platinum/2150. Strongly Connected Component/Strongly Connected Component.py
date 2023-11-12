# 2150 Strongly Connected Component

from collections import defaultdict
from sys import setrecursionlimit, stdin
setrecursionlimit(10**5)


def input():
    return stdin.readline().strip()


class Tarjan:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.index = 0
        self.indexs = [-1] * self.vertices
        self.low = [0] * self.vertices
        self.on_stack = [False] * self.vertices
        self.stack = []
        self.scc_count = 0
        self.sccs = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, current_node):
        self.stack.append(current_node)
        self.on_stack[current_node] = True
        self.index += 1
        self.indexs[current_node] = self.low[current_node] = self.index

        for next_node in self.graph[current_node]:
            if self.indexs[next_node] == -1:
                self.dfs(next_node)
            if self.on_stack[next_node]:
                self.low[current_node] = min(
                    self.low[current_node], self.low[next_node]
                )

        # Start of a strongly connected component
        if self.indexs[current_node] == self.low[current_node]:
            component = []
            while True:
                node = self.stack.pop()
                component.append(node)
                self.on_stack[node] = False
                self.low[node] = self.indexs[current_node]
                if node == current_node:
                    break
            self.scc_count += 1
            self.sccs.append(component)

    def find_sccs(self):
        for i in range(self.vertices):
            if self.indexs[i] == -1:
                self.dfs(i)
        return self.sccs


V, E = map(int, input().split())
tarjan = Tarjan(vertices=V + 1)
edges = [tuple(map(int, input().split())) for _ in range(E)]
for u, v in edges:
    tarjan.add_edge(u, v)
sccs = tarjan.find_sccs()
for i, v in enumerate(sccs):
    sccs[i] = sorted(v)
sccs.sort(key=lambda x: x[0])
print(len(sccs) - 1)
for v in sccs:
    if v == [0]:
        continue
    print(*v, -1)