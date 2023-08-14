# 17069 파이프 옮기기 2
from itertools import product

N = int(input())
grid = [list(map(int, input().split(" "))) for _ in range(N)]
# Y축 -> X축 -> 방향 : 가로 0 세로 1 대각선 2
answer = [[[0] * 3 for _ in range(N)] for _ in range(N)]
answer[0][1][0] = 1
for i, j in product(range(N), range(2, N)):
    if grid[i][j] == 0:
        answer[i][j][0] = answer[i][j - 1][2] + answer[i][j - 1][0]
    if grid[i][j] == 0:
        answer[i][j][1] = answer[i - 1][j][1] + answer[i - 1][j][2]
    if grid[i][j] == 0 and grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
        answer[i][j][2] = (
            answer[i - 1][j - 1][0] + answer[i - 1][j - 1][1] + answer[i - 1][j - 1][2]
        )
print(sum(answer[-1][-1]))
