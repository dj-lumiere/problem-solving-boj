from itertools import permutations, combinations
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n, m = int(input()), int(input())
        counts = [dict() for _ in range(m)]
        for _ in range(n):
            name = input()
            for i, ch in enumerate(name):
                counts[i][ch] = counts[i].get(ch, 0) + 1
        county_name = ''
        for count in counts:
            max_freq = -1
            selected_char = ''
            for ch in sorted(count.keys()):
                if count[ch] > max_freq:
                    max_freq = count[ch]
                    selected_char = ch
            county_name += selected_char
        answer = county_name
        answers.append(f"{answer}")
    print(*answers, sep="\n")