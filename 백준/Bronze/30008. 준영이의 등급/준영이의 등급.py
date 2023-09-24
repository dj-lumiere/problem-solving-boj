# B번 - 준영이의 등급


def grade(p):
    if p <= 4:
        return 1
    if p <= 11:
        return 2
    if p <= 23:
        return 3
    if p <= 40:
        return 4
    if p <= 60:
        return 5
    if p <= 77:
        return 6
    if p <= 89:
        return 7
    if p <= 96:
        return 8
    return 9


N, K = map(int, input().split(" "))
rank = list(map(int, input().split(" ")))
print(*[grade((i * 100) // N) for i in rank])