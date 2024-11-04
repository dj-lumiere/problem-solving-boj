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
    t = 1
    answers = []
    for hh in range(t):
        base2_wrong = input()
        base3_wrong = input()
        n1 = set()
        for i in range(len(base2_wrong)):
            flipped = list(base2_wrong)
            flipped[i] = '1' if flipped[i] == '0' else '0'
            n1.add(int(''.join(flipped), 2))
        n2 = set()
        for i in range(len(base3_wrong)):
            for d in ['0','1','2']:
                if base3_wrong[i] != d:
                    changed = list(base3_wrong)
                    changed[i] = d
                    n2.add(int(''.join(changed), 3))
        intersection = n1 & n2
        if len(intersection) ==1:
            answer = intersection.pop()
            answers.append(f"{answer}")
    print(*answers, sep="\n")