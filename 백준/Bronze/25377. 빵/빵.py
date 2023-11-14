# 25377 빵

N = int(input())
stores = [tuple(map(int, input().split(" "))) for _ in range(N)]
availability = [B for A, B in stores if A <= B]
print(min(availability) if availability else -1)