from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    t = int(input())
    answers = []
    president_values = {"Franklin":100, "Grant":50, "Jackson":20, "Hamilton":10, "Lincoln":5, "Washington":1}
    for hh in range(t):
        names = input().split()
        total = sum(president_values[name] for name in names)
        answer = f"${total}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")