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
        N = input()
        M = input()


        def process(num_str):
            return list(map(int, num_str[::-1]))


        N_digits = process(N) if N else []
        M_digits = process(M) if M else []
        max_len = max(len(N_digits), len(M_digits))
        new_N = []
        new_M = []
        for i in range(max_len):
            d1 = N_digits[i] if i < len(N_digits) else 0
            d2 = M_digits[i] if i < len(M_digits) else 0
            if d1 < d2:
                new_N.append(None)
                new_M.append(d2)
            elif d1 > d2:
                new_N.append(d1)
                new_M.append(None)
            else:
                new_N.append(d1)
                new_M.append(d2)


        def reconstruct(digits):
            filtered = [str(d) for d in digits if d is not None]
            if not filtered:
                return "YODA"
            return str(int(''.join(filtered[::-1])))


        result_N = reconstruct(new_N)
        result_M = reconstruct(new_M)
        answer = f"{result_N}\n{result_M}"
        answers.append(answer)
    print(*answers, sep="\n")