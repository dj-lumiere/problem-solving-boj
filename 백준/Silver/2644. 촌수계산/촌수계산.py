# 2644 촌수계산
from collections import deque

N = int(input())
a, b = list(map(int, input().split(" ")))
m = int(input())
relations = {i: [] for i in range(1, N + 1)}
for _ in range(m):
    i, j = list(map(int, input().split(" ")))
    relations[i].append(j)
    relations[j].append(i)

# 깊이 우선 탐색으로 친척관계가 뻗어나가는지 확인
def dfs(i, j) -> bool:
    visited = [False for _ in range(N + 1)]
    stack = [i]
    while stack:
        next_node = stack.pop()
        for i in relations[next_node]:
            stack.append(i)
            if not visited[i]:
                visited[i] = True
            else:
                stack.pop()
    return visited[j]


# 만약 상대방이 보이면 친척 단계 구하기
def bfs(i, j) -> int:
    queue = deque()
    queue.append((i, 0))
    while queue:
        x, y = queue.popleft()
        if x == j:
            return y
        else:
            for i in relations[x]:
                queue.append((i, y + 1))


if dfs(a, b):
    print(bfs(a, b))
else:
    print(-1)