from sys import setrecursionlimit, stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        x, y = int(input()), int(input())
        results = {}
        stack = [(x, y)]
        while stack:
            n, k = stack.pop()
            eprint(n, k)
            if (n, k) in results:
                continue
            elif 1 < n < k:
                # try to find (n-1, k)
                if n - 1 == 1:
                    results[(n, k)] = k % n
                elif k == 1:
                    results[(n, k)] = (n - 1 + k) % n
                elif (n - 1, k) in results:
                    results[(n, k)] = (results[(n - 1, k)] + k) % n
                else:
                    stack.append((n, k))
                    stack.append((n - 1, k))
            else:
                # try to find (n-n//k, k)
                h = 0
                next_n, next_k = n - n // k, k
                if (next_n, next_k) in results:
                    h = results[(next_n, next_k)]
                elif next_n == 1:
                    h = 0
                elif next_k == 1:
                    h = next_n - 1
                elif 1 < next_n < next_k and (next_n - 1, next_k) in results:
                    h = (results[(next_n - 1, next_k)] + next_k) % n
                else:
                    stack.append((n, k))
                    stack.append((next_n, next_k))
                    continue
                h -= (n % k)
                if h < 0:
                    results[(n, k)] = h + n
                else:
                    results[(n, k)] = h + h // (k - 1)
        answer = results[(n, k)] + 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")
