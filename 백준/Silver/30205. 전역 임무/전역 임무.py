# 30205 전역 임무

from sys import stdin


def input():
    return stdin.readline().strip()


N, M, P = map(int, input().split(" "))
s = [sorted(list(map(int, input().split(" ")))) for _ in range(N)]
can_be_cleared = 1
for s_sub in s:

    item_count = 0
    for i, base in enumerate(s_sub):
        if base == -1:
            item_count += 1
            s_sub[i] = 0

    for base in s_sub:
        while item_count > 0 and base > P:
            item_count -= 1
            P *= 2
        if base > P:
            can_be_cleared = 0
        else:
            P += base

    if item_count:
        P *= 2**item_count

    if not can_be_cleared:
        break

print(can_be_cleared)