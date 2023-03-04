# 14889 스타트와 링크

N = int(input())
S = [list(map(int, input().split(" "))) for i in range(N)]
ability_difference = 123904834690845390563123123


def team_maker(N: int, M: int) -> list[list[int]]:
    list_permut = []
    stack = [False for _ in range(N)]

    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            stack = [False for _ in range(N)]
            return
        else:
            # 조합
            for i in range(init, N):
                stack[i] = True
                dfs(i + 1, M - 1, stack)
                stack[i] = False

    dfs(0, M, stack)
    return list_permut


def permut(N: int, M: int) -> list[list[int]]:
    list_permut = []
    stack = []

    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            # 조합
            for i in range(init, N):
                stack.append(i)
                dfs(i + 1, M - 1, stack)
                stack.pop()

    dfs(0, M, stack)
    return list_permut


team_list = team_maker(N, N // 2)
permut_list = permut(N // 2, 2)
for team in team_list:
    start_team = [i for (i, j) in enumerate(team) if j]
    link_team = [i for (i, j) in enumerate(team) if not j]
    start_team_score = 0
    link_team_score = 0
    for (i, j) in permut_list:
        start_team_score += (
            S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]
        )
        link_team_score += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]
    ability_difference_sub = abs(start_team_score - link_team_score)
    if ability_difference > ability_difference_sub:
        ability_difference = ability_difference_sub
print(ability_difference)