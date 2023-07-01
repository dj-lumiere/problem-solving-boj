# 28298 더 흔한 타일 색칠 문제
from itertools import product

N, M, K = map(int, input().split(" "))
grid = [list(input()) for _ in range(N)]
answer = 0
for x_sub, y_sub in product(range(K), range(K)):
    element_frequency = [0] * 26
    frequent_element_index = -1
    frequent_element_frequency = -1
    for x_pos, y_pos in product(range(x_sub, M, K), range(y_sub, N, K)):
        element_frequency[ord(grid[y_pos][x_pos]) - ord("A")] += 1
    for index, value in enumerate(element_frequency):
        if frequent_element_frequency < value:
            frequent_element_index, frequent_element_frequency = index, value
    answer += N * M // K // K - frequent_element_frequency
    for x_pos, y_pos in product(range(x_sub, M, K), range(y_sub, N, K)):
        grid[y_pos][x_pos] = chr(ord("A") + frequent_element_index)
print(answer, *["".join(sub_list) for sub_list in grid], sep="\n")