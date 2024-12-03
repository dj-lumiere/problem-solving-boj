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
        n = int(input())
        m = int(input())
        database = [tuple(int(input()) for _ in range(m)) for _ in range(n)]
        q = int(input())
        for _ in range(q):
            query = tuple(int(input()) for _ in range(m))
            count = 0
            for row in database:
                match = True
                for a, b in zip(row, query):
                    if b != -1 and a != b:
                        match = False
                        break
                if match:
                    count += 1
            answer = f"{count}"
            answers.append(f"{answer}")
    print(*answers, sep="\n")