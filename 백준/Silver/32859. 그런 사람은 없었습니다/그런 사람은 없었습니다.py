from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
    for hh in range(t):
        n, m = (int(input()), int(input()))
        s = int(input())
        money_send = [False for _ in range(n + 1)]
        form_send = [False for _ in range(n + 1)]
        people = [set() for _ in range(n + 1)]
        for _ in range(m):
            i, j = int(input()), int(input())
            if j == 1:
                money_send[i] = True
            elif j == 0:
                form_send[i] = True
                for k in range(n + 1):
                    if money_send[k] and not form_send[k]:
                        people[k].add(i)
        result = []
        for i, v in enumerate(people):
            if len(v) >= s and i != 0:
                result.append(i)
        if not result:
            result.append(-1)
        answer = "\n".join(map(str, result))
        answers.append(f"{answer}")
    print(*answers, sep="\n")