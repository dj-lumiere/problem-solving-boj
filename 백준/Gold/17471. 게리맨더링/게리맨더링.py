from itertools import product

n = int(input())
quantity = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
min_difference = 10**6
separation_possible = False
for i in range(1, n+1):
    x, *y = map(int, input().split())
    graph[i].extend(y)
    for y2 in y:
        graph[y2].append(i)
for i, v in enumerate(graph):
    graph[i] = sorted(set(v))
for mask in range(1 << n):
    group1 = [False] + [mask & (1 << i) != 0 for i in range(n)]
    group2 = [False] + [mask & (1 << i) == 0 for i in range(n)]
    if all(not i for i in group1[1:]):
        continue
    if all(not i for i in group2[1:]):
        continue
    is_accessible_group1 = [False for _ in range(n+1)]
    is_accessible_group2 = [False for _ in range(n+1)]
    visited1 = [False for _ in range(n + 1)]
    visited2 = [False for _ in range(n + 1)]
    stack1 = [i for i, v in enumerate(group1) if v][:1]
    stack2 = [i for i, v in enumerate(group2) if v][:1]
    if stack1:
        visited1[stack1[0]] = True
        is_accessible_group1[stack1[0]] = True
    if stack2:
        visited2[stack2[0]] = True
        is_accessible_group2[stack2[0]] = True
    while stack1:
        current = stack1.pop()
        for i in graph[current]:
            if visited1[i]:
                continue
            if not group1[i]:
                continue
            is_accessible_group1[i] = is_accessible_group1[current] = True
            visited1[i] = True
            stack1.append(i)
    while stack2:
        current = stack2.pop()
        for i in graph[current]:
            if visited2[i]:
                continue
            if not group2[i]:
                continue
            is_accessible_group2[i] = is_accessible_group2[current] = True
            visited2[i] = True
            stack2.append(i)
    is_all_accessible1 = True
    is_all_accessible2 = True
    for i in range(n+1):
        if group1[i] and not is_accessible_group1[i]:
            is_all_accessible1 = False
        if group2[i] and not is_accessible_group2[i]:
            is_all_accessible2 = False
    if not is_all_accessible1 or not is_all_accessible2:
        continue
    separation_possible = True
    group1_quantity = sum(i*j for i, j in zip(quantity, group1))
    group2_quantity = sum(i*j for i, j in zip(quantity, group2))
    min_difference = min(min_difference, abs(group1_quantity - group2_quantity))
print(min_difference if separation_possible else -1)