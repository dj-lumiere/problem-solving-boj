# 11566 킥

N = int(input())
dream_pattern = list(map(int, input().split()))
M = int(input())
sound_pattern = list(map(int, input().split()))
answer = []
for i in range(1, M + 1):
    for j in range(M):
        for k in range(N):
            if j + i * k >= M:
                break
            if sound_pattern[j + i * k] != dream_pattern[k]:
                break
        else:
            answer.append(i - 1)
if not answer:
    print(-1)
else:
    print(min(answer), max(answer))
