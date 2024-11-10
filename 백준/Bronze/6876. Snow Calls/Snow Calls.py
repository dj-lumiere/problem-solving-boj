from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = int(input())
    mapping = {}
    for letters, digit in zip(['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'], range(2, 10)):
        for letter in letters:
            mapping[letter] = str(digit)
    answers = []
    for _ in range(t):
        s = input()
        digits = ''.join([mapping[c] if c.isalpha() else c for c in s if c != '-'])[:10]
        formatted = f"{digits[:3]}-{digits[3:6]}-{digits[6:10]}"
        answer = formatted
        answers.append(f"{answer}")
    print(*answers, sep="\n")