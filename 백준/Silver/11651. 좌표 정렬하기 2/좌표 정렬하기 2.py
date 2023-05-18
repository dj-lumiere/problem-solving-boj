# 11651 좌표 정렬하기 2

from sys import stdin

N: int = int(stdin.readline().strip())
coordination_list: list[tuple[int, int]] = []
for i in range(N):
    x, y = map(int, stdin.readline().strip().split(" "))
    coordination_list.append((x, y))
coordination_list = sorted(coordination_list, key=lambda x: (x[1], x[0]))
print(*[f"{i} {j}" for (i, j) in coordination_list], sep="\n")
