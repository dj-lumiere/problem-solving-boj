from itertools import product

t = int(input())
answers = []
for hh in range(1, t + 1):
    v, e, a, b = map(int, input().split())
    trees = list(map(int, input().split()))
    parents = [0 for _ in range(v + 1)]
    time_in = [0] * (v + 1)
    time_out = [0] * (v + 1)
    for i, j in zip(trees[::2], trees[1::2]):
        parents[j] = i
    graph = [[] for _ in range(v + 1)]
    for i, j in enumerate(parents[1:], start=1):
        if i == 1:
            continue
        graph[j].append(i)
        graph[i].append(j)
    time = 0
    root = 1
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if not visited:
            time += 1
            time_in[node] = time
            stack.append((node, True))
            for child in reversed(graph[node]):
                if time_in[child] == 0:
                    stack.append((child, False))
        else:
            time_out[node] = time
    visited = [False for _ in range(v + 1)]
    visited[root] = True
    depth = [0] * (v + 1)
    stack2 = [root]
    while stack2:
        node = stack2.pop()
        for child in graph[node]:
            if visited[child]:
                continue
            depth[child] = depth[node] + 1
            visited[child] = True
            stack2.append(child)
    MAX_STEP = 20
    ancestor_power_of_2 = [[0 for _ in range(v + 1)] for _ in range(MAX_STEP)]
    ancestor_power_of_2[0] = parents[:]
    for i, j in product(range(1, MAX_STEP), range(1, v + 1)):
        ancestor_power_of_2[i][j] = ancestor_power_of_2[i - 1][ancestor_power_of_2[i - 1][j]]
    lca = 0
    if depth[a] > depth[b]:
        a, b = b, a
    for step in reversed(range(MAX_STEP)):
        if depth[b] - depth[a] >= 2 ** step:
            b = ancestor_power_of_2[step][b]
    if a == b:
        lca = a
    else:
        for step in reversed(range(MAX_STEP)):
            if ancestor_power_of_2[step][a] != ancestor_power_of_2[step][b]:
                a = ancestor_power_of_2[step][a]
                b = ancestor_power_of_2[step][b]
        lca = ancestor_power_of_2[0][a]
    answer = f"{lca} {time_out[lca] - time_in[lca] + 1}"
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")