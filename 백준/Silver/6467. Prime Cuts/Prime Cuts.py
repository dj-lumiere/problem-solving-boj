from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


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
    t = INF
    answers = []
    for hh in range(t):
        N = input()
        C = input()
        if N is None or C is None:
            break
        N = int(N)
        C = int(C)
        primes = [1]
        for num in range(2, N + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        length = len(primes)
        if length == 0:
            center = []
        elif length % 2 == 1:
            start = max(0, length // 2 - (C - 1))
            end = min(length, length // 2 + C)
            center = primes[start:end]
        else:
            start = max(0, length // 2 - C)
            end = min(length, length // 2 + C)
            center = primes[start:end]
        if len(center) > 2 * C and length % 2 == 0:
            center = primes
        elif len(center) > (2 * C - 1) and length % 2 == 1:
            center = primes
        output = f"{N} {C}:"
        for num in center:
            output += f" {num}"
        answer = output
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")