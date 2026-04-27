from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, m = (int(input()) for _ in range(2))
        s = input()
        deleted = [False for _ in range(n)]
        letter = {}
        for i, v in enumerate(s):
            if v not in letter:
                letter[v] = []
            letter[v].append(i)
        for k in letter:
            letter[k].sort(reverse=True)
        for _ in range(m):
            min_letter = min(letter.keys())
            idx = letter[min_letter].pop()
            if not letter[min_letter]:
                letter.__delitem__(min_letter)
            deleted[idx] = True
        answer = "".join([v for i, v in enumerate(s) if not deleted[i]])
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")