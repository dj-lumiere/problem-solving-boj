import re
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
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
        words = [input() for _ in range(n)]
        tokens = [re.split(r"([A-Za-z]+)", i) for i in words]
        for i, v in enumerate(tokens):
            tokens[i] = [j for j in v if j]
            for j, v2 in enumerate(tokens[i]):
                if not v2.isalpha():
                    tokens[i][j] = (0, [int(v2), len(v2) - len(str(int(v2)))])
                else:
                    tokens[i][j] = (1, [(ord(v3.upper()) - ord("A")) * 2 + (v3.islower()) for v3 in v2])
        tokens.sort()
        result = []
        for i, v in enumerate(tokens):
            result_sub = ""
            for j, (k, v2) in enumerate(v):
                if k == 1:
                    for v3 in v2:
                        digit, mode = divmod(v3, 2)
                        char = chr(ord("A") + digit)
                        result_sub += (char.lower() if mode else char)
                else:
                    number, trailing_zero = v2
                    result_sub += "0" * trailing_zero + str(number)
            result.append(result_sub)
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")
