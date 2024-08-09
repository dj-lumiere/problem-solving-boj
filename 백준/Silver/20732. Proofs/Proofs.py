from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        answer = "correct"
        assumptions = set()
        for i in range(1, n + 1):
            statement = input().split()
            arrow_index = statement.index("->")
            assumption = statement[:arrow_index]
            conclusion = statement[arrow_index + 1:]
            if not assumption:
                for v in conclusion:
                    assumptions.add(v)
                continue
            if all(i in assumptions for i in assumption):
                for v in conclusion:
                    assumptions.add(v)
            else:
                answer = f"{i}"
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")
