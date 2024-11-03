from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        m = int(input())
        if m < 2:
            answer = "none"
        else:
            freq = {}
            max_x = -1
            limit = int(m ** (1/3)) + 2
            for a in range(1, limit):
                a_cubed = a ** 3
                if a_cubed > m:
                    break
                for b in range(a, limit):
                    s = a_cubed + b ** 3
                    if s > m:
                        break
                    freq[s] = freq.get(s, 0) + 1
                    if freq[s] == 2 and s > max_x:
                        max_x = s
            answer = max_x if max_x != -1 else "none"
        answers.append(f"{answer}")
    print(*answers, sep="\n")