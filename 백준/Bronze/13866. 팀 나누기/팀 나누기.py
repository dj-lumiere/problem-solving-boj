# 13866 팀 나누기

from itertools import permutations

skill_level = list(map(int, input().split(" ")))
skill_level_difference = [
    abs(a + b - c - d) for a, b, c, d in permutations(skill_level)
]
print(min(skill_level_difference))