# 15460 My Cow Ate My Homework
from fractions import Fraction

N = int(input())
homework_score = list(map(int, input().split(" ")))
homework_accumulated_sum = [sum(homework_score)]
local_minimal_point = [10001]
local_minimal_sub = 10001
for i, v in enumerate(reversed(homework_score)):
    if v < local_minimal_sub:
        local_minimal_sub = v
    local_minimal_point.append(local_minimal_sub)
local_minimal_point.reverse()
maximum_indices = []
maximum_average_score = Fraction(-1)
for v in homework_score:
    homework_accumulated_sum.append(homework_accumulated_sum[-1] - v)
for i, (local_min, total_score) in enumerate(
    zip(local_minimal_point, homework_accumulated_sum)
):
    if i == 0 or i + 1 >= N:
        continue
    average_score = Fraction(total_score - local_min, N - i - 1)
    if average_score > maximum_average_score:
        maximum_indices.clear()
        maximum_average_score = average_score
    if average_score == maximum_average_score:
        maximum_indices.append(i)
print(*maximum_indices, sep="\n")