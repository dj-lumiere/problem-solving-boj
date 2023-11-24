# 1389 케빈 베이컨의 6단계 법칙

INF = 10**18
user, node = list(map(int, input().split(" ")))
graph = [[] for i in range(user + 1)]
distance = [[INF for _ in range(user + 1)] for _ in range(user + 1)]
for _ in range(node):
    i, j = list(map(int, input().split(" ")))
    graph[i].append(j)
    graph[j].append(i)
    distance[i][j] = 1
    distance[j][i] = 1
for mid in range(1, user + 1):
    for start in range(1, user + 1):
        for end in range(1, user + 1):
            distance[start][end] = min(
                distance[start][end], distance[start][mid] + distance[mid][end]
            )
answer = []
for i in range(1, user + 1):
    answer_sub = []
    for j in range(1, user + 1):
        if i == j:
            continue
        answer_sub.append(distance[i][j])
    answer.append(sum(answer_sub))
print(answer.index(min(answer)) + 1)
