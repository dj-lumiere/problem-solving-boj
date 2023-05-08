# 18111 마인크래프트

from sys import stdin

N, M, B = (int(i) for i in stdin.readline().strip().split(" "))
INT_MAX = N * M * 256 * 2
ground_level = [[int(i) for i in stdin.readline().strip().split(" ")] for _ in range(N)]
minimum_ground_level = min((min(ground_level[i]) for i in range(N)))
maximum_ground_level = max((max(ground_level[i]) for i in range(N)))
minimum_time = INT_MAX
leveled_height = 0
for target_height in range(minimum_ground_level, maximum_ground_level + 1):
    ground_to_etch = 0
    ground_to_fill = 0
    for r in range(N):
        for c in range(M):
            if target_height > ground_level[r][c]:
                ground_to_fill += target_height - ground_level[r][c]
            elif target_height < ground_level[r][c]:
                ground_to_etch += ground_level[r][c] - target_height
    if ground_to_fill > B + ground_to_etch:
        continue
    else:
        answer_sub = ground_to_etch * 2 + ground_to_fill * 1
        if minimum_time >= answer_sub:
            leveled_height = target_height
            minimum_time = answer_sub
print(minimum_time, leveled_height)