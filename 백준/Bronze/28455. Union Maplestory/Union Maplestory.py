# 28455 Union Maplestory


def find_ability_increment(level: int) -> int:
    result = 0
    if level >= 60:
        result += 1
    if level >= 100:
        result += 1
    if level >= 140:
        result += 1
    if level >= 200:
        result += 1
    if level >= 250:
        result += 1
    return result


N = int(input())
levels = [int(input()) for _ in range(N)]
levels.sort(reverse=True)
levels = levels[:42]
print(sum(levels), sum(map(find_ability_increment, levels)))