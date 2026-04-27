# 29700 우당탕탕 영화예매
from itertools import product

N, M, K = map(int, input().split(" "))
seat = [list(map(int, list(input()))) for _ in range(N)]
result = 0
for y, x in product(range(N), range(M)):
    if x + K > M:
        continue
    if not any(seat[y][x : x + K]):
        result += 1
print(result)
