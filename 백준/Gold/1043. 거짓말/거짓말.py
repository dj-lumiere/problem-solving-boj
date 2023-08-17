# 1043 거짓말

from sys import stdin


def input():
    return stdin.readline().strip()


def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        parent[root_x] = root_y


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


N, M = map(int, input().split(" "))
_, *truth = list(map(int, input().split(" ")))
parties = []
parent = [i for i in range(N + 1)]
for _ in range(M):
    _, *party = list(map(int, input().split(" ")))
    parties.append(party)
for party in parties:
    for i in range(len(party) - 1):
        union(party[i], party[i + 1], parent)
truth_set = set()
for person in truth:
    truth_set.add(find(person, parent))
result = sum(1 for party in parties if find(party[0], parent) not in truth_set)
print(result)