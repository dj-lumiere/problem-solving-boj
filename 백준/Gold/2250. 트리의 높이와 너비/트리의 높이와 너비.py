from collections import deque
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        tree = [[int(input()) - 1 for _ in range(3)] for _ in range(n)]
        tree.sort(key=lambda x: x[0])
        parent = [-1 for _ in range(n)]
        graph = [[] for _ in range(n)]
        stack = []
        for a, b, c in tree:
            if b != -2:
                parent[b] = a
                graph[a].append(b)
                graph[b].append(a)
            if c != -2:
                parent[c] = a
                graph[a].append(c)
                graph[c].append(a)
            if b == c == -2:
                stack.append(a)
        eprint(f"{parent=}")
        level = [0 for _ in range(n)]
        subtree_length = [[1, 0, 0] for _ in range(n)]
        position = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        root = 0
        for i in range(n):
            if parent[i] == -1:
                root = i
                break
        queue = deque([root])
        visited[root] = True
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                level[next_node] = level[node] + 1
                queue.append(next_node)
        while stack:
            node = stack.pop()
            parent_node = parent[node]
            if parent_node == -1:
                continue
            stack.append(parent_node)
            if tree[parent_node][1] == node:
                subtree_length[parent_node][1] = subtree_length[node][0]
            if tree[parent_node][2] == node:
                subtree_length[parent_node][2] = subtree_length[node][0]
            subtree_length[parent_node][0] = subtree_length[parent_node][1] + subtree_length[parent_node][2] + 1
        position[root] = subtree_length[root][1] + 1
        queue = deque([root])
        while queue:
            i = queue.popleft()
            _, b, c = tree[i]
            if b != -2:
                position[b] = position[i] - subtree_length[b][2] - 1
                queue.append(b)
            if c != -2:
                position[c] = position[i] + subtree_length[c][1] + 1
                queue.append(c)
        max_level = max(level)
        width_max = -INF
        width_max_level = -INF
        for i in reversed(range(max_level + 1)):
            level_width = [k for j, k in zip(level, position) if j == i]
            current_level_width = max(level_width) - min(level_width) + 1
            if current_level_width >= width_max:
                width_max = current_level_width
                width_max_level = i + 1
        answer = f"{width_max_level} {width_max}"
        answers.append(answer)
    print(*answers, sep="\n")