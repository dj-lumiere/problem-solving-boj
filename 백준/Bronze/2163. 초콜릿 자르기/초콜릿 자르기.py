# 2163 초콜릿 자르기

N, M = list(map(int, input().split(" ")))
print(min((N - 1) + N * (M - 1), (M - 1) + M * (N - 1)))