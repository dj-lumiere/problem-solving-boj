# 11054 가장 긴 바이토닉 부분 수열

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

N = int(input().strip())
A = list(map(int, input().strip().split(" ")))


def lis_length(A: list[int]) -> list[int]:
    lis_length = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                lis_length[i] = max(lis_length[i], lis_length[j] + 1)
    return lis_length


# 특정 시점을 기준으로 LIS와 LDS를 찾는데,
# k번째로 바이토닉을 찾을 땐 k번째까지의 LIS와 n~k번째까지의 LIS

lis = lis_length(A)
lds = list(reversed(lis_length(list(reversed(A)))))
bitonic_length = [
    lis_element + lds_element - 1 for lis_element, lds_element in zip(lis, lds)
]
print(f"{max(bitonic_length)}")