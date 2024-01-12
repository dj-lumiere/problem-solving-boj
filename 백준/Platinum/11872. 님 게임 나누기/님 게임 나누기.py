# 11872 님 게임 나누기

from functools import reduce


def find_grundy_number(rocks):
    # 4k+3인 경우랑 4k+4인 경우가 값이 뒤바뀜 (k=0,1,2,3,...)
    if rocks % 4 == 3:
        return rocks + 1
    if rocks and rocks % 4 == 0:
        return rocks - 1
    return rocks


N = int(input())
P = list(map(int, input().split()))
P_grundy_numbers = list(map(find_grundy_number, P))
print("koosaga" if reduce(lambda x, y: x ^ y, P_grundy_numbers) else "cubelover")