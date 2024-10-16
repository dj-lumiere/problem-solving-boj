from sys import stderr, stdout

with open(0, "r") as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = INF
    answers = []
    for hh in range(1, x + 1):
        queries = []
        query_sub = []
        while s := input():
            if s == "0":
                break
            if s.isdigit():
                query_sub.append(int(s))
            else:
                query_sub.append(s)
                queries.append(query_sub[:])
                query_sub = []
            if s == "right on":
                break
        if not queries:
            break
        is_lying = False
        i = queries[-1][0]
        for j, v in queries[:-1]:
            if i > j and v != "too low":
                is_lying = True
                break
            if i < j and v != "too high":
                is_lying = True
                break
            if i == j and v != "right on":
                is_lying = True
                break
        if is_lying:
            answers.append("Stan is dishonest")
        else:
            answers.append("Stan may be honest")
    print(*answers, sep="\n")