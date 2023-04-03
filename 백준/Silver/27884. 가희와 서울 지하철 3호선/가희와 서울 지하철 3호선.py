# D번 - 가희와 서울 지하철 3호선

# bruteforcing으로 rollercoaster 구간의 길이 구하기
# 조건을 만족하면 갯수 세기

# 순열, 중복순열, 조합, 중복조합 (백트래킹)


def permut(N: int, M: int) -> list[list[int]]:
    list_permut = []
    stack = []

    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            # 중복순열
            for i in range(1, N + 1):
                stack.append(i)
                dfs(i, M - 1, stack)
                stack.pop()

    dfs(1, M, stack)

    return list_permut


def roller_coaster_length(level: list[int]) -> int:
    answer_dp = [0 for i in range(len(level))]
    for (i, j) in enumerate(level):
        if i == 0:
            answer_dp[i] = 1
        else:
            if j != level[i - 1]:
                answer_dp[i] = answer_dp[i - 1] + 1
            else:
                answer_dp[i] = 1
    return max(answer_dp)


mod: int = 10**9 + 7
n, m = list(map(int, input().split(" ")))
station_name_list = [input() for _ in range(n)]
level_list: list[list[int]] = permut(2, n)
answer: int = 0
for level_sublist in level_list:
    answer_sub: int = 1
    if roller_coaster_length(level_sublist) == m:
        for level in level_sublist:
            answer_sub *= 11 if level == 2 else 5
        answer += answer_sub
        answer %= mod
print(answer)