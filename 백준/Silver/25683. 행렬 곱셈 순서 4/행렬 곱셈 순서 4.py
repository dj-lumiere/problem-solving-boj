# 25683 행렬 곱셈 순서 4

from sys import stdin


def input():
    return stdin.readline().strip()


N = int(stdin.readline())
matrix_size = []
answer = 0
for _ in range(N):
    matrix_size.append(tuple(map(int, input().split(" "))))
while len(matrix_size) > 1:
    size2_row, size2_col = matrix_size.pop()
    size1_row, size1_col = matrix_size.pop()
    answer += size1_row * size1_col * size2_col
    matrix_size.append((size1_row, size2_col))
print(answer)