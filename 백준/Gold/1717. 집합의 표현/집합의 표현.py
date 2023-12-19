# 1717 집합의 표현

from sys import stdin


def input():
    return stdin.readline().strip()


class DisjointSet:
    def __init__(self, node_count):
        self.node_count = node_count
        self.parent = [i for i in range(self.node_count + 1)]
        self.rank = [0 for _ in range(self.node_count + 1)]

    def union(self, x, y):
        root_x = self.find_parent(x)
        root_y = self.find_parent(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

    def find_parent(self, x):
        nodes = []
        while x != self.parent[x]:
            nodes.append(x)
            x = self.parent[x]
        for node in nodes:
            self.parent[node] = x
        return x

    def is_connected(self, a, b):
        parent_a = self.find_parent(a)
        parent_b = self.find_parent(b)
        return parent_a == parent_b


n, m = map(int, input().split(" "))
sets = DisjointSet(n + 1)
for _ in range(m):
    opcode, *operand = map(int, input().split(" "))
    if opcode == 0:
        sets.union(*operand)
    if opcode == 1:
        print("YES" if sets.is_connected(*operand) else "NO")
