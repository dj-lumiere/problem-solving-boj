# 15718 돌아온 떡파이어
# 뤼카 정리 활용
from random import randint


def n_ary_change(x: int, n: int) -> list[int]:
    next_x = x
    change_list = []
    while next_x:
        change_list.append(next_x % n)
        next_x //= n
    return change_list[::-1]


nCr_list: list[list[int]] = [[] for n in range(1031)]
for n in range(1031):
    for r in range(1031+1):
        if n < r:
            nCr_list[n].append(0)
        elif r != 0 and r != n:
            nCr_list[n].append((nCr_list[n - 1][r - 1] + nCr_list[n - 1][r]) % 100007)
        else:
            nCr_list[n].append(1)


test_case = int(input())
for i in range(test_case):
    # 100007 = 97*1031이므로 각각에 대해 뤼카 정리와 중국인의 나머지 정리 적용
    N, M = list(map(int, input().split(" ")))
    A, B = N - 1, M - 2
    # M-1일간 N개의 떡국을 먹어야함
    # 다만 M-1개의 떡국은 미리 소비되어야하니 그걸 제외하고 소비해야함
    # nHr(M-1, N-(M-1)) = nCr(N-M+1+M-1-1, N-M+1)=nCr(N-1, M-2)
    if A == -1 and B == -1:
        print(1)
    elif B > A or A < 0 or B < 0:
        print(0)
    else:
        a_list1 = n_ary_change(A, 97)
        b_list1 = n_ary_change(B, 97)
        a_list2 = n_ary_change(A, 1031)
        b_list2 = n_ary_change(B, 1031)
        if len(a_list1) > len(b_list1):
            b_list1 = [0] * (len(a_list1) - len(b_list1)) + b_list1
        if len(a_list2) > len(b_list2):
            b_list2 = [0] * (len(a_list2) - len(b_list2)) + b_list2
        mod_97 = 1
        for n, r in zip(a_list1, b_list1):
            mod_97 = (mod_97 * nCr_list[n][r]) % 97
        mod_1031 = 1
        for n, r in zip(a_list2, b_list2):
            mod_1031 = (mod_1031 * nCr_list[n][r]) % 1031
        print(
            (mod_1031 * 97 * pow(97, -1, 1031) + mod_97 * 1031 * pow(1031, -1, 97))
            % 100007
        )