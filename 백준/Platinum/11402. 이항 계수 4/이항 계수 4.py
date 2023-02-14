# 11402 이항 계수 4
# 뤼카 정리 활용
from time import perf_counter
from sys import setrecursionlimit

setrecursionlimit(10**9)


def n_ary_change(x, n) -> list[int]:
    next_x = x
    change_list = []
    while next_x:
        change_list.append(next_x % n)
        next_x //= n
    return change_list[::-1]


A, B, C = list(map(int, input().split(" ")))

dp_list = [[0 for i in range(j + 1)] for j in range(C + 1)]


def nCr(n: int, r: int) -> int:
    if r == 0:
        dp_list[n][r] = 1
        dp_list[n][n - r] = 1
    elif r == 1:
        dp_list[n][r] = n
        dp_list[n][n - r] = n
    elif r > n // 2:
        if dp_list[n][n - r] != 0:
            dp_list[n][r] = dp_list[n][n - r]
        else:
            dp_list[n][r] = nCr(n, n - r)
    else:
        if dp_list[n - 1][r] != 0:
            a = dp_list[n - 1][r]
        else:
            a = nCr(n - 1, r)
        if dp_list[n - 1][r - 1] != 0:
            b = dp_list[n - 1][r - 1]
        else:
            b = nCr(n - 1, r - 1)
        dp_list[n][r] = (a + b) % C
        dp_list[n][n - r] = (a + b) % C
    return dp_list[n][r]

a_list = n_ary_change(A, C)
b_list = n_ary_change(B, C)
if len(a_list) > len(b_list):
    b_list = [0] * (len(a_list) - len(b_list)) + b_list

answer = 1
for i, j in zip(a_list, b_list):
    if i < j:
        answer *= 0
        break
    else:
        factor = nCr(i, j)
        answer *= factor
        answer %= C
print(answer)