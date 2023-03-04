# 7568 덩치

N = int(input())
body_spec = [tuple(map(int, input().split(" "))) for _ in range(N)]
body_spec_rank = [1 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if body_spec[i][0] < body_spec[j][0] and body_spec[i][1] < body_spec[j][1]:
            body_spec_rank[i] += 1
print(*body_spec_rank)