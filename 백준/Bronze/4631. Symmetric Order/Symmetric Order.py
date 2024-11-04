from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    answers = []
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        strings = [input() for _ in range(n)]
        output = []
        for i in range(n//2):
            output.append(strings.pop(i))
        output.extend(strings[::-1])
        answer = f"SET {hh + 1}\n" + '\n'.join(output)
        answers.append(f"{answer}")
    print(*answers, sep="\n")