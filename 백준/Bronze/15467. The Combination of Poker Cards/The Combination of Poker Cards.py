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
        cards = [int(input()) for _ in range(6)]
        freq = {}
        for card in cards:
            freq[card] = freq.get(card, 0) + 1
        counts = list(freq.values())
        counts.sort(reverse=True)
        if counts == [1, 1, 1, 1, 1, 1]:
            answer = "single"
        elif counts == [2, 1, 1, 1, 1]:
            answer = "one pair"
        elif counts == [2, 2, 1, 1]:
            answer = "two pairs"
        elif counts == [2, 2, 2]:
            answer = "three pairs"
        elif counts == [3, 1, 1, 1]:
            answer = "one triple"
        elif counts == [3, 3]:
            answer = "two triples"
        elif counts == [4, 1, 1]:
            answer = "tiki"
        elif counts == [4, 2]:
            answer = "tiki pair"
        elif counts == [3, 2, 1]:
            answer = "full house"
        else:
            answer = "unknown"
        answers.append(f"{answer}")
    print(*answers, sep="\n")