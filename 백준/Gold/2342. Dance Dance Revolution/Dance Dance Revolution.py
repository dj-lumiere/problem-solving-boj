# 2342 Dance Dance Revolution

from sys import maxsize
from itertools import product

ILLEGAL: int = maxsize >> 3
CENTER: int = 2
SAME: int = 1
ADJACENT: int = 3
OPPOSITE: int = 4

step: list[int] = list(map(int, input().split(" ")))
step.pop()
length: int = len(step)

# current a -> next b movement cost = moving_force[a][b]
moving_force: list[list[int]] = [
    [ILLEGAL, CENTER, CENTER, CENTER, CENTER],
    [ILLEGAL, SAME, ADJACENT, OPPOSITE, ADJACENT],
    [ILLEGAL, ADJACENT, SAME, ADJACENT, OPPOSITE],
    [ILLEGAL, OPPOSITE, ADJACENT, SAME, ADJACENT],
    [ILLEGAL, ADJACENT, OPPOSITE, ADJACENT, SAME],
]

# force_dp[n][L][R] = force required to nth step with position L at left feet and R at right feet
force_dp: list[list[list[int]]] = [
    [[ILLEGAL for r in range(5)] for l in range(5)] for n in range(length)
]
current_l_pos = 0
current_r_pos = 0

force_dp[0][0][step[0]] = CENTER
force_dp[0][step[0]][0] = CENTER

for i, prev_lstep, prev_rstep, curr_lstep, curr_rstep in product(
    range(length), range(5), range(5), range(5), range(5)
):
    if i == 0:
        continue
    if curr_lstep != step[i] and curr_rstep != step[i]:
        continue
    if prev_lstep != curr_lstep and prev_rstep != curr_rstep:
        continue
    if prev_lstep == curr_lstep and prev_rstep == curr_rstep:
        force_dp[i][curr_lstep][curr_rstep] = min(
            force_dp[i][curr_lstep][curr_rstep],
            force_dp[i - 1][prev_lstep][prev_rstep]
            + moving_force[prev_lstep][curr_lstep],
            force_dp[i - 1][prev_lstep][prev_rstep]
            + moving_force[prev_rstep][curr_rstep],
        )
    elif prev_lstep != curr_lstep and prev_rstep == curr_rstep:
        force_dp[i][curr_lstep][curr_rstep] = min(
            force_dp[i][curr_lstep][curr_rstep],
            force_dp[i - 1][prev_lstep][prev_rstep]
            + moving_force[prev_lstep][curr_lstep],
        )
    elif prev_lstep == curr_lstep and prev_rstep != curr_rstep:
        force_dp[i][curr_lstep][curr_rstep] = min(
            force_dp[i][curr_lstep][curr_rstep],
            force_dp[i - 1][prev_lstep][prev_rstep]
            + moving_force[prev_rstep][curr_rstep],
        )

print(min([force_dp[-1][i][j] for i, j in product(range(5), range(5))]))