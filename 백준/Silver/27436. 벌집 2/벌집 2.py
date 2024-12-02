from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
    for _ in range(t):
        N = int(input())
        target = N - 1
        left = 0
        right = 5000000000
        while left + 1 < right:
            mid = (left + right) // 2
            val = 6 * mid * (mid + 1) // 2
            if val >= target:
                right = mid
            else:
                left = mid
        k = right + 1 if N != 1 else 1
        answer = k
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")