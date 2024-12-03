from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        encrypted = input()
        schools = {'nlcs': 'northlondoncollegiateschool', 'bha': 'branksomehallasia', 'kis': 'koreainternationalschool', 'sja': 'stjohnsburyacademy'}
        found = False
        for abbrev, fullname in schools.items():
            processed = ''.join(filter(str.isalpha, fullname)).lower()[:10]
            for N in range(26):
                shifted = ''.join([chr((ord(char) - ord('a') + N) % 26 + ord('a')) for char in processed])
                if shifted == encrypted:
                    answer = abbrev.upper()
                    found = True
                    break
            if found:
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")