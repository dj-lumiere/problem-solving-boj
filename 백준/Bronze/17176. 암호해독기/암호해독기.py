from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
        n = int(input())
        cipher = list(map(int, input().split()))
        plain = input()
        eprint(plain)
        plain_nums = []
        for ch in plain:
            if ch == ' ':
                plain_nums.append(0)
            elif 'A' <= ch <= 'Z':
                plain_nums.append(ord(ch) - ord('A') + 1)
            elif 'a' <= ch <= 'z':
                plain_nums.append(ord(ch) - ord('a') + 27)
        eprint(plain_nums)
        count_cipher = [0] * 53
        count_plain = [0] * 53
        for num in cipher:
            count_cipher[num] += 1
        for num in plain_nums:
            count_plain[num] += 1
        answer = "y" if count_cipher == count_plain else "n"
        answers.append(f"{answer}")
    print(*answers, sep="\n")