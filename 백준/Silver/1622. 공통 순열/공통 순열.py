from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = INF
    answers = []
    for hh in range(t):
        a = input()
        b = input()
        if a is None and b is None:
            break
        count_a = [0] * 26
        count_b = [0] * 26
        for c in a:
            count_a[ord(c) - 97] += 1
        for c in b:
            count_b[ord(c) - 97] += 1
        x = ''.join([chr(i + 97) * min(count_a[i], count_b[i]) for i in range(26)])
        answer = x
        answers.append(f"{answer}")
    print(*answers, sep="\n")