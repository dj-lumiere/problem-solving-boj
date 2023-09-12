# 20303 할로윈의 양아치

from sys import stdin
from itertools import product


def input():
    return stdin.readline().strip()


N, M, K = map(int, input().split(" "))
visited = [False] * (N + 1)
candy_count = [0] + list(map(int, input().split(" ")))
relations = [[] for _ in range(N + 1)]
candies_in_group = []

for _ in range(M):
    a, b = map(int, input().split(" "))
    relations[a].append(b)
    relations[b].append(a)

for i in range(1, N + 1):
    if visited[i]:
        continue
    group_size = 1
    group_candy_count = 0
    stack = [i]
    visited[i] = True
    while stack:
        current_friend = stack.pop()
        group_candy_count += candy_count[current_friend]
        for next_friend in relations[current_friend]:
            if visited[next_friend]:
                continue
            stack.append(next_friend)
            visited[next_friend] = True
            group_size += 1
    if group_size >= K:
        continue
    candies_in_group.append((group_size, group_candy_count))

group_count = len(candies_in_group)
dp = [[0 for _ in range(K)] for _ in range(group_count + 1)]
for i, j in product(range(group_count + 1), range(K)):
    if i == 0 or j == 0:
        continue
    group_size, group_candy_count = candies_in_group[i - 1]
    if j >= group_size:
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - group_size] + group_candy_count)
    else:
        dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])