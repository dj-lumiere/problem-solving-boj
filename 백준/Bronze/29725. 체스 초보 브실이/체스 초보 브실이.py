# 29725 체스 초보 브실이

from collections import Counter

grid = []
for _ in range(8):
    grid.extend(list(input()))
grid_counter = Counter(grid)
white_score = 0
black_score = 0
white_score_dict = {"K": 0, "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9}
black_score_dict = {"k": 0, "p": 1, "n": 3, "b": 3, "r": 5, "q": 9}
for k, v in white_score_dict.items():
    white_score += grid_counter[k] * v
for k, v in black_score_dict.items():
    black_score += grid_counter[k] * v
print(white_score - black_score)
