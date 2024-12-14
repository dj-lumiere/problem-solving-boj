from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        count = 0
        for p in range(3, n + 1):
            if sieve[p] and p != 2 and p != 5:
                remainder = 1 % p
                k = 1
                while True:
                    remainder = (remainder * 10) % p
                    k += 1
                    if k > 2 * p:
                        break
                    remainder = (remainder * 10 + 1) % p
                    k += 1
                    if remainder == 0:
                        if k == p - 2:
                            count += 1
                        break
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")