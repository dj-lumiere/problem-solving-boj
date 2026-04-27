from math import log


def factorial_zeroes(N: int) -> int:
    if not N:
        return 0
    count_2 = 0
    count_5 = 0
    maximum_power_2 = int(log(N, 2))
    maximum_power_5 = int(log(N, 5))
    for i in range(1, maximum_power_2 + 1):
        count_2 += (N // (2 ** i))
    for i in range(1, maximum_power_5 + 1):
        count_5 += (N // (5 ** i))
    return min(count_2, count_5)


N = int(input())
start = 0
end = 5 * N + 1
while start + 1 < end:
    mid = (start+end)//2
    if factorial_zeroes(mid) >= N:
        end = mid
    else:
        start = mid
if factorial_zeroes(end) != N:
    end = -1
print(end)