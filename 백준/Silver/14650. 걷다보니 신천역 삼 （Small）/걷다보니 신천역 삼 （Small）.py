# 14650 걷다보니 신천역 삼 (Small)

N = int(input())
answer = [[0 for _ in range(3)] for _ in range(N)]
answer[0][1] = answer[0][2] = 1
for i in range(1, N):
    for j in range(3):
        for k in range(3):
            answer[i][(j * 10 + k) % 3] += answer[i - 1][j]
print(answer[-1][0])