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
    t = int(input())
    answers = []
    for hh in range(t):
        L = int(input())
        U = int(input())
        max_divisors = 0
        for num in range(L, U + 1):
            if num == 1:
                count = 1
            else:
                count = 2
                sqrt_num = int(num ** 0.5)
                for i in range(2, sqrt_num + 1):
                    if num % i == 0:
                        if i == num // i:
                            count += 1
                        else:
                            count += 2
            if count > max_divisors:
                max_divisors = count
        answer = f"{max_divisors}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")