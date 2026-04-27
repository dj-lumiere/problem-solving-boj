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
        k = int(input())
        a = [int(input()) for _ in range(n)]
        group = [0 for _ in range(n)]
        table = []
        group_count = 1
        for i in range(n):
            if group[i] != 0:
                continue
            table.append([])
            group[i] = group_count
            table[-1].append(i)
            stack = [i]
            while stack:
                cur = stack.pop()
                nxt = (cur + k) % n
                if group[nxt] != 0:
                    continue
                group[nxt] = group_count
                table[-1].append(nxt)
                stack.append(nxt)
            table[-1].sort()
            group_count += 1
        k_sorted_a = a[:]
        for v in table:
            sub_group = v
            sub_a = [a[v2] for v2 in v]
            sub_a.sort()
            for i, v2 in enumerate(v):
                k_sorted_a[v2] = sub_a[i]
        sorted_a = sorted(a)
        if k_sorted_a == sorted_a:
            answers.append("YES")
        else:
            answers.append("NO")
    print(*answers, sep="\n")