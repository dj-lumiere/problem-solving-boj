# 28453 Previous Level


def find_level_zone(level: int) -> int:
    if level == 300:
        return 1
    if 275 <= level < 300:
        return 2
    if 250 <= level < 275:
        return 3
    return 4


N = int(input())
level = list(map(int, input().split(" ")))
print(*map(find_level_zone, level))