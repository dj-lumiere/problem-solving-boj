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
    t = int(input())
    answers = []
    for hh in range(t):
        secret_str = input()
        guess_str = input()
        circles = 0
        squares = 0
        secret_used = [False] * 4
        guess_used = [False] * 4
        for i in range(4):
            if secret_str[i] == guess_str[i]:
                circles += 1
                secret_used[i] = True
                guess_used[i] = True
        for i in range(4):
            if not guess_used[i]:
                for j in range(4):
                    if not secret_used[j] and guess_str[i] == secret_str[j]:
                        squares += 1
                        secret_used[j] = True
                        break
        answer = f"For secret = {secret_str} and guess = {guess_str}, {circles} circles and {squares} squares will light up."
        answers.append(f"{answer}")
    print(*answers, sep="\n")