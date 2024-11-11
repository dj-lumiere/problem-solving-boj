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
    for hh in range(t):
        n = int(input())
        digits = [input() for _ in range(n)]
        digit_sequence = ''.join(digits)
        substring_set = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring_set.add(int(digit_sequence[i:j]))
        k = 0
        while True:
            if k not in substring_set:
                answer = k
                break
            k += 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")