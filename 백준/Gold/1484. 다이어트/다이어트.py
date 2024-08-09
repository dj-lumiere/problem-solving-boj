from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
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
        # x^2-y^2=g?
        # (x+y)(x-y)=g => j*i=g
        # x=(i+j)//2
        factors = []
        for i in range(1, int(n ** .5) + 1):
            if n % i != 0:
                continue
            factors.append(i)
        possible_weight = []
        for i in factors:
            j = n // i
            if i % 2 != j % 2:
                continue
            x = (i + j) // 2
            y = j - x
            if y == 0:
                continue
            possible_weight.append(x)
        possible_weight.sort()
        result = "\n".join(map(str, possible_weight)) if possible_weight else "-1"
        answer = f"{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
