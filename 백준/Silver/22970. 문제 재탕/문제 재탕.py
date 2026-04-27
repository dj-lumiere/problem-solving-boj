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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        answer = 0
        n = int(input())
        a = [int(input()) for _ in range(n)]
        for i in range(n):
            left = a[:i]
            pivot = a[i]
            right = a[i + 1:]
            left_dec_length = 0
            left_value = pivot
            right_dec_length = 0
            right_value = pivot
            for j, v in enumerate(reversed(left)):
                if v >= left_value:
                    break
                left_value = v
                left_dec_length += 1
            for j, v in enumerate(right):
                if v >= right_value:
                    break
                right_value = v
                right_dec_length += 1
            answer_sub = left_dec_length + right_dec_length + 1
            answer = max(answer, answer_sub)
        answers.append(f"{answer}")
    print(*answers, sep="\n")