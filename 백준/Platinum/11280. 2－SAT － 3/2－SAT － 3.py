# 11280 2-SAT - 3

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
        self.scc_index = [0] * self.vertices
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
        self.indexs[current_node] = self.low[current_node] = self.index
        self.index += 1

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
                self.scc_index[node] = self.scc_count
                if node == current_node:
                    break
            self.scc_count += 1
            self.sccs.append(component)

    def find_sccs(self):
        for i in range(self.vertices):
            if self.indexs[i] == -1:
                self.dfs(i)
        return self.sccs


def convert_if_negative(u):
    return (abs(u) - 1) * 2 + (1 if u < 0 else 0)


def negate(u):
    return u ^ 1


N, M = map(int, input().split())
tarjan = Tarjan(vertices=2 * N)
edges = [tuple(map(int, input().split())) for _ in range(M)]

for u, v in edges:
    u = convert_if_negative(u)
    v = convert_if_negative(v)
    tarjan.add_edge(negate(u), v)
    tarjan.add_edge(negate(v), u)

sccs = tarjan.find_sccs()

for i in range(N):
    if tarjan.scc_index[2 * i] == tarjan.scc_index[2 * i + 1]:
        print(0)
        break
else:
    print(1)