# 2875 대회 or 인턴

N, M, K = map(int, input().split(" "))
max_teams = -1
for i in range(K + 1):
    woman_teamable = (N - i) // 2
    man_teamable = M - (K - i)
    max_teams = max(max_teams, min(woman_teamable, man_teamable))
print(max_teams)