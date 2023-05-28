# 18870 좌표 압축
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input())
X = list(map(int, input().strip().split(" ")))
result = [0 for _ in range(N)]
X_sorted = sorted(list(set(X)))
X_rank = {value: index for index, value in enumerate(X_sorted)}
for index, value in enumerate(X):
    result[index] = X_rank[value]
result_str = " ".join(map(str, result))
print(f"{result_str}")