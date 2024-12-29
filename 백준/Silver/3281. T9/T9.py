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
    letter_to_key = {}
    key_mapping = {
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
    }
    for key, letters in key_mapping.items():
        for letter in letters:
            letter_to_key[letter] = key
    for hh in range(t):
        M = int(input())
        dict_words = [input() for _ in range(M)]
        N = int(input())
        keys = [input() for _ in range(N)]
        sequence_to_word = {}
        for word in dict_words:
            key_seq = tuple(letter_to_key.get(c, '1') for c in word)
            if key_seq not in sequence_to_word:
                sequence_to_word[key_seq] = word
        groups = []
        current = []
        for k in keys:
            if k == '1':
                if current:
                    groups.append(current)
                    current = []
            else:
                current.append(k)
        if current:
            groups.append(current)
        message_words = []
        for group in groups:
            key_tuple = tuple(group)
            if key_tuple in sequence_to_word:
                message_words.append(sequence_to_word[key_tuple])
            else:
                message_words.append('*' * len(group))
        message = ' '.join(message_words)
        answer = message
        answers.append(f"{answer}")
    print(*answers, sep="\n")