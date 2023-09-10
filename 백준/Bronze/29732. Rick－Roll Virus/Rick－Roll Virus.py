# 29732 Rick-Roll Virus

N, M, K = map(int, input().split(" "))
current_virus = list(input())
next_day_virus = [0] * N
for i, v in enumerate(current_virus):
    if v == "R":
        for j in range(max(0, i - K), min(N, i + K + 1)):
            next_day_virus[j] = 1
if sum(next_day_virus) <= M:
    print("Yes")
else:
    print("No")
