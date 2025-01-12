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
        if n % 2 == 1:
            m = (n // 2) * (n // 2 + 1)
        else:
            m = (n // 2) * (n // 2 - 1) + n // 2
        answer = [f"{m}"]
        if m <= 1000000:
            sub_interval_count = []
            if n % 2 == 1:
                sub_interval_count.extend(range(1, n // 2 + 1))
                sub_interval_count.extend(reversed(range(1, n // 2 + 1)))
            else:
                sub_interval_count.extend(range(1, n // 2 + 1))
                sub_interval_count.extend(reversed(range(1, n // 2)))
            for i in range(1, n):
                sub_interval_length = sub_interval_count[i - 1]
                sub_interval = [[] for _ in range(sub_interval_length)]
                idx = 0
                for j in range(1, n - i + 1):
                    sub_interval[idx].append(f"{j} {j + i}")
                    idx += 1
                    idx %= sub_interval_length
                for v in sub_interval:
                    answer.append(f"{len(v)} " + " ".join(v))
        answers.extend(answer)
    print(*answers, sep="\n")