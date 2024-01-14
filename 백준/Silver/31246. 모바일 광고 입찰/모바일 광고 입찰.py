# 31246 모바일 광고 입찰

N, K = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(N)]
start = -1
end = 10**9 + 1
while start + 1 < end:
    mid = (start + end) >> 1
    binded_papers = 0
    for a, b in prices:
        if a + mid >= b:
            binded_papers += 1
    if binded_papers >= K:
        end = mid
    else:
        start = mid
print(end)