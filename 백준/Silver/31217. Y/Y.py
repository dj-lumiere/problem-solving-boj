# 31217 Y

from math import comb

MOD = 10**9 + 7
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
for i, v in enumerate(graph):
    if i == 0:
        continue
    node_count = len(v)
    if node_count < 3:
        continue
    result += (node_count * (node_count - 1) * (node_count - 2) // 6) % MOD
    result %= MOD
print(result)