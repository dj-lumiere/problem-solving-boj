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
    t = int(input())
    answers = []
    for _ in range(t):
        word = input()
        word_upper = word.upper()
        freq = {}
        for c in word_upper:
            if 'A' <= c <= 'Z':
                freq[c] = freq.get(c, 0) + 1
        is_opposite = True
        for c in freq:
            opposite_c = chr(ord('A') + ord('Z') - ord(c))
            if freq.get(opposite_c, 0) != freq[c]:
                is_opposite = False
                break
        answer = "Yes" if is_opposite else "No"
        answers.append(f"{answer}")
    print(*answers, sep="\n")