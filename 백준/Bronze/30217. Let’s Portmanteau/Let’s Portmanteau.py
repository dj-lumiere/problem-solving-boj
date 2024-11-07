from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        word1 = input()
        word2 = input()
        letters1 = word1[0]
        v1 = ''
        for c in word1[1:]:
            if c in 'aeiou':
                v1 = c
                break
            letters1 += c
        letters2 = ''
        v2 = ''
        for c in reversed(word2[:-1]):
            if c in 'aeiou':
                v2 = c
                break
            letters2 += c
        letters2 = letters2[::-1] + word2[-1]
        if v2:
            mv = v2
        elif v1:
            mv = v1
        else:
            mv = 'o'
        combined = letters1 + mv + letters2
        answer = combined
        answers.append(f"{answer}")
    print(*answers, sep="\n")