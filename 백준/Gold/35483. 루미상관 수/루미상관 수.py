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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = int(input())
    answers = []
    soomisanggwan_numbers = set()
    for i in range(1, 10):
        soomisanggwan_numbers.add(i)
    for i in range(1, 10 ** 5):
        soomisanggwan_numbers.add(int(str(i) + str(i)))
        for j in range(10):
            soomisanggwan_numbers.add(int(str(i) + str(j) + str(i)))
    for hh in range(1, t + 1):
        n = int(input())
        answer = 0
        for i in soomisanggwan_numbers:
            if i > n:
                continue
            if n - i in soomisanggwan_numbers:
                answer += 1
        answers.append(answer)
    print(*answers, sep="\n")