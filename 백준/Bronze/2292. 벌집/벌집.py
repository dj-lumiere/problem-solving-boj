# 2292 벌집

level = 0
last_level_in_number = 1
n = int(input())
while last_level_in_number < n:
    level += 1
    last_level_in_number += level * 6
print(level + 1 if n != 1 else 1)