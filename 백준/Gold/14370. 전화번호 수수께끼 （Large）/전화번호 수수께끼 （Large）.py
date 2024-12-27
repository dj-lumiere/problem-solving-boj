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
    unique = ["Z", "O", 'W', 'H', 'U', 'F', 'X', 'S', 'G', 'I']
    word = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    process_order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    answers = []
    for hh in range(t):
        s = input()
        freq = [s.count(chr(ord("A") + i)) for i in range(26)]
        result = [0 for _ in range(10)]
        for i in process_order:
            j, k = ord(unique[i]) - ord("A"), word[i]
            unique_count = freq[j]
            result[i] += unique_count
            for v in map(lambda x: ord(x) - ord("A"), k):
                freq[v] -= unique_count
        answer = f"Case #{hh + 1}: " + "".join(map(lambda x: f"{x[0]}" * x[1], enumerate(result)))
        answers.append(f"{answer}")
    print(*answers, sep="\n")