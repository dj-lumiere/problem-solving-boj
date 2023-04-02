# 10971 외판원 순회 2

from functools import lru_cache

N = int(input())
W = [list(map(int, input().split(" "))) for _ in range(N)]
default_value = 1000000 * (N + 1) + 1
tsp_dp = [[default_value for _ in range((1 << N))] for _ in range(N)]


@lru_cache(maxsize=None)
def tsp(visited: int, current_city: int) -> int:
    if visited == (1 << N) - 1:
        return W[current_city][0] if W[current_city][0] != 0 else default_value
    elif tsp_dp[current_city][visited] != default_value:
        return tsp_dp[current_city][visited]
    answer_sub = default_value
    for next_city in range(N):
        if not (visited & (1 << next_city)) and W[current_city][next_city] != 0:
            answer_sub = min(
                answer_sub,
                tsp(visited | (1 << next_city), next_city) + W[current_city][next_city],
            )
    tsp_dp[current_city][visited] = answer_sub
    return answer_sub


print(tsp(1, 0))