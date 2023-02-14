from sys import setrecursionlimit

setrecursionlimit(10**9)

A, B = list(map(int, input().split(" ")))
C = 10007
dp_list = [[0 for i in range(j + 1)] for j in range(A + 1)]


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
print(nCr(A, B))