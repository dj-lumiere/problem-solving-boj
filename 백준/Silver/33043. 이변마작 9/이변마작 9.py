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
    t = 1
    answers = []
    available_cards = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '1p', '2p', '3p', '4p', '5p', '6p', '7p',
                       '8p', '9p', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '1z', '2z', '3z', '4z', '5z',
                       '6z', '7z']
    for hh in range(t):
        n = int(input())
        cards = [input() for _ in range(n)]
        card_sum = [{i: 0 for i in available_cards} for _ in range(n + 1)]
        for i, card in enumerate(cards, start=1):
            card_sum[i] = card_sum[i - 1].copy()
            card_sum[i][card] += 1
        if all(v <= 4 for v in card_sum[-1].values()):
            answer = "-1"
        else:
            answer = INF
            for i, card in enumerate(cards, start=1):
                start = i - 1
                end = n + 1
                if all(v2 - v1 <= 4 for v1, v2 in zip(card_sum[start].values(), card_sum[n].values())):
                    continue
                while start + 1 < end:
                    mid = (start + end) // 2
                    current_card_count = card_sum[mid][card] - card_sum[i - 1][card]
                    if current_card_count <= 4:
                        start = mid
                    else:
                        end = mid
                answer = min(answer, end - i + 1)
        answers.append(f"{answer}")
    print(*answers, sep="\n")