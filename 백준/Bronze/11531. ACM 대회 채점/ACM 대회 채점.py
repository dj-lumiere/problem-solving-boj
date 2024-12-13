from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    submissions = []
    for hh in range(t):
        while True:
            m = input()
            if m is None:
                break
            if m == '-1':
                break
            problem = input()
            result = input()
            submissions.append((int(m), problem, result))
        processed = {}
        for i, (m, p, r) in enumerate(submissions):
            key = (m, p)
            if key not in processed:
                processed[key] = []
            processed[key].append(i)
        valid = [True] * len(submissions)
        for key, indices in processed.items():
            if len(indices) > 1:
                for idx in indices[:-1]:
                    valid[idx] = False
        solved = {}
        wrongs = {}
        total_penalty = 0
        for i, (m, p, r) in enumerate(submissions):
            if not valid[i]:
                r = 'wrong'
            if p in solved:
                continue
            if r == 'right':
                solved[p] = m
                total_penalty += m + wrongs.get(p, 0) * 20
            else:
                wrongs[p] = wrongs.get(p, 0) + 1
        answer = f"{len(solved)} {total_penalty}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")