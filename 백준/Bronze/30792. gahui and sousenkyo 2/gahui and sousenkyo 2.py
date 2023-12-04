# B번 - gahui and sousenkyo 2

n = int(input())
a = int(input())
others = list(map(int, input().split(" "))) + [a]
others.sort(reverse=True)
rank = {v: i for i, v in enumerate(others, start=1)}
print(rank[a])