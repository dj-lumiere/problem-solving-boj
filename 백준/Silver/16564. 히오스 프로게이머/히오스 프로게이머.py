# 16564 히오스 프로게이머

from sys import stdin

N, K = list(map(int, stdin.readline().rstrip().split(" ")))
current_level_list = [int(stdin.readline().rstrip()) for _ in range(N)]
start = 0
end = max(current_level_list) + K
result = 0
while start <= end:
    mid = (start + end) // 2
    required_point = sum([max(0, mid - i) for i in current_level_list])
    if required_point <= K:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
