# 3079 입국심사

from sys import stdin

N, M = list(map(int, stdin.readline().rstrip().split(" ")))
time_list = [int(stdin.readline().rstrip()) for _ in range(N)]

start = 0
end = 10**18
result = 0
while start <= end:
    mid = (start + end) // 2
    total_person = sum([mid // i for i in time_list])
    if total_person >= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)
