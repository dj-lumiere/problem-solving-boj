from decimal import getcontext
from sys import stderr, stdout

getcontext().prec = 30


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
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []


    def number_to_words(x):
        word = []
        while x > 0:
            x, d = divmod(x, 26)
            word.append(chr(ord('a') + d))
        word += ["a"] * 13
        word = word[:13]
        word.reverse()
        return "".join(word)


    def words_to_number(words):
        result = 0
        for word in words:
            result *= 26
            result += ord(word) - ord("a")
        return result


    for _ in range(t):
        T = int(input())
        if T == 1:
            A = int(input())
            B = int(input())
            S = A + B
            word_str = number_to_words(S)
            answer = word_str
        elif T == 2:
            s = input()
            S = words_to_number(s)
            answer = str(S)
        answers.append(f"{answer}")
    print(*answers, sep="\n")