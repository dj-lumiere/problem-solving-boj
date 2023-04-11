# C번 - 하이퍼 가지 따기
from collections import Counter
from sys import stdin

entrance_trial_list: list[list[int]] = [
    list(map(int, stdin.readline().strip().split(" "))) for i in range(2047)
]
entrance_list: list[dict[int, int]] = [
    Counter([entrance_trial_list[j][i] for j in range(2047)]) for i in range(11)
]
not_tried_list = [
    [i for (i, j) in entrance_list[k].items() if j == 1023][0] for k in range(11)
]
print(*not_tried_list)